from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import redirect, render

from .forms import (
    CreateGroupForm,
    FriendsForm,
    GroupCheckForm,
    GroupSelectForm,
    PostForm,
)
from .models import Friend, Good, Group, Message


# Create your views here.
# indexのビュー関数
@login_required(login_url="/admin/login/")
def index(request, page=1):
    # publicユーザーの取得
    (public_user, public_group) = get_public()

    # POST時の処理
    if request.method == "POST":
        # Groups のチェックを更新したときの処理
        # フォームの用意
        checkform = GroupCheckForm(request.user, request.POST)
        # チェックされたGroup名をリストにまとめる
        glist = []
        for item in request.POST.getlist("groups"):
            glist.append(item)
        # Messageの取得
        messages = get_your_group_message(request.user, glist, page)

    # GET時の処理
    else:
        # フォームの用意
        checkform = GroupCheckForm(request.user)
        # Groupのリストを取得
        gps = Group.objects.filter(owner=request.user)
        glist = [public_group.title]
        for item in gps:
            glist.append(item.title)
        # メッセージの取得
        messages = get_your_group_message(request.user, glist, page)

    params = {
        "login_user": request.user,
        "contents": messages,
        "check_form": checkform,
    }
    return render(request, "sns/index.html", params)


# グループの表示
@login_required(login_url="/admin/login/")
def groups(request):
    # 自分が登録したFriendを取得
    friends = Friend.objects.filter(owner=request.user)

    # POST送信時の処理
    if request.method == "POST":

        # Groupsメニュー選択肢の処理
        if request.POST["mode"] == "__groups_form__":
            # 選択したGroup名を取得
            sel_group = request.POST["groups"]
            # Groupsを取得
            gp = Group.objects.filter(title=sel_group).first()
            # Groupに含まれるFriendの取得
            fds = Friend.objects.filter(owner=request.user).filter(group=gp)
            print(Friend.objects.filter(owner=request.user))
            # FriendのUserをリストにまとめる
            vlist = []
            for item in fds:
                vlist.append(item.user.username)
            # formの用意
            groupsform = GroupSelectForm(request.user, request.POST)
            friendsform = FriendsForm(
                request.user, friends=friends, vals=vlist
            )

        # Friendsのチェック更新時の処理
        if request.POST["mode"] == "__friends_form__":
            # 選択したGroupの取得
            sel_group = request.POST["groups"]
            group_obj = Group.objects.filter(title=sel_group).first()
            print(group_obj)
            # チェックしたFriendの取得
            sel_fds = request.POST.getlist("friends")
            # FriendsのUserを取得
            sel_users = User.objects.filter(username__in=sel_fds)
            # Userのリストに含まれるユーザーが登録したFriendを取得
            fds = Friend.objects.filter(owner__in=request.user).filter(
                user__in=sel_users
            )
            # すべてのFriendにGroupを設定し、保存する
            vlist = []
            for item in fds:
                item.group = group_obj
                item.save()
                vlist.append(item.user.username)
            # メッセージを設定
            messages.success(
                request, " チェックされたFriendを " + sel_group + " に登録しました"
            )
            # フォームの用意
            groupsform = GroupSelectForm(request.user, {"groups": sel_group})
            friendsform = FriendsForm(
                request.user, friends=friends, vals=vlist
            )

    # GETアクセス時の処置
    else:
        # フォームの用意
        groupsform = GroupSelectForm(request.user)
        friendsform = FriendsForm(request.user, friends=friends, vals=[])
        sel_group = "-"

    # 共通の処理
    createform = CreateGroupForm()
    params = {
        "login_user": request.user,
        "groups_form": groupsform,
        "friends_form": friendsform,
        "create_form": createform,
        "group": sel_group,
    }
    return render(request, "sns/groups.html", params)


# Friendの追加処理
@login_required(login_url="/admin/login/")
def add(request):
    # 追加するUserの取得
    add_name = request.GET["name"]
    add_user = User.objects.filter(username=add_name).first()
    # Userが本人だった場合の処理
    if add_user == request.user:
        messages.info(request, "自分自身をFriendに登録することはできません。")
        return redirect(to="/sns")

    # publicの取得
    (_, public_group) = get_public()
    # add_userのFriendの数を調べる
    frd_num = (
        Friend.objects.filter(owner=request.user).filter(user=add_user).count()
    )
    # 0より大きければ、すでに登録済み
    if frd_num > 0:
        messages.info(request, add_user.name + "はすでに追加されています")
        return redirect(to="/sns")

    # Friendの登録処理
    frd = Friend()
    frd.owner = request.user
    frd.user = add_user
    frd.group = public_group
    frd.save()
    # メッセージを設定
    messages.success(
        request,
        add_user.username + "を追加しました! groupページに移動して、追加したFriendをメンバーに追加してください",
    )
    return redirect(to="/sns")


# グループの作成処理
@login_required(login_url="/admin/login/")
def creategroup(request):
    # Groupを作成し、Userとtitleを設定して保存する
    group = Group()
    group.owner = request.user
    group.title = request.user.username + "の" + request.POST["group_name"]
    group.save()
    messages.info(request, "新しいグループを作成しました。")
    return redirect(to="/sns/groups")


# メッセージのポスト処理
@login_required(login_url="/admin/login/")
def post(request):
    # POST送信の処理
    if request.method == "POST":
        # 送信内容の取得
        gr_name = request.POST["groups"]
        content = request.POST["content"]
        # Groupの取得
        group = (
            Group.objects.filter(owner=request.user)
            .filter(title=gr_name)
            .first()
        )
        # 検索してGroupが無ければ、publicへ
        if group is None:
            (_, group) = get_public()

        # Messageを作成し設定して保存
        msg = Message()
        msg.owner = request.user
        msg.group = group
        msg.content = content
        msg.save()
        # メッセージを設定
        messages.success(request, "新しいメッセージを投稿しました！")
        return redirect(to="/sns")

    # GETアクセス時の処理
    else:
        form = PostForm(request.user)

    # 共通処理
    params = {
        "login_user": request.user,
        "form": form,
    }
    return render(request, "sns/post.html", params)


# 投稿をシェアする
@login_required(login_url="/admin/login/")
def share(request, share_id):
    # シェアするメッセージの取得
    share = Message.objects.get(id=share_id)
    print(share)

    # POST送信時の処理
    if request.method == "POST":
        # 送信内容の確認
        gr_name = request.POST["groups"]
        content = request.POST["content"]
        # Groupの取得
        group = (
            Group.objects.filter(owner=request.user)
            .filter(title=gr_name)
            .first()
        )
        if group is None:
            (_, group) = get_public()
        # メッセージを作成し、設定をして保存
        msg = Message()
        msg.owner = request.user
        msg.group = group
        msg.content = content
        msg.share_id = share.id
        msg.save()
        # メッセージを設定
        messages.success(request, "メッセージをシェアしました！")
        return redirect(to="/sns")

    # 共通処理
    form = PostForm(request.user)

    # 共通処理
    params = {"login_user": request.user, "form": form, "share": share}
    return render(request, "sns/share.html", params)


# goodボタンの処理
@login_required(login_url="/admin/login/")
def good(request, good_id):
    # goodするメッセージの取得
    good_msg = Message.objects.get(id=good_id)
    # 自分がメッセージにGoodした数を数える
    is_good = (
        Good.objects.filter(owner=request.user)
        .filter(message=good_msg)
        .count()
    )
    # 0より大きければgood済み
    if is_good > 0:
        messages.success(request, "すでにメッセージにgoodしています")
        return redirect(to="/sns")

    # Messageのgood_countを1増やす
    good_msg.good_count += 1
    good_msg.save()
    # Goodを作成し、保存
    good = Good()
    good.owner = request.user
    good.message = good_msg
    good.save()
    # メッセージの作成
    messages.success(request, "メッセージにGoodしました")

    return redirect(to="/sns")


# -----------------------------------------------------------------
# 普通の関数
# -----------------------------------------------------------------
# public_user, public_group を取得する
def get_public():
    public_user = User.objects.filter(username="public").first()
    public_group = Group.objects.filter(owner=public_user).first()
    return (public_user, public_group)


# 指定されたグループおよび検索文字によるMessageの取得
def get_your_group_message(owner, glist, page):
    # 1ページあたりの表示数
    page_num = 10
    # publicの取得
    (public_user, _) = get_public()
    # チェックされたGroupの取得
    groups = Group.objects.filter(
        Q(owner=owner) | Q(owner=public_user)
    ).filter(title__in=glist)
    # Groupに含まれるFriendの取得
    me_friends = Friend.objects.filter(group__in=groups)
    # FriendのUserをリストにまとめる
    me_users = []
    for f in me_friends:
        me_users.append(f.user)
    # UserリストのUserが作ったGroupの取得
    his_groups = Group.objects.filter(owner__in=me_users)
    his_friends = Friend.objects.filter(user=owner).filter(
        group__in=his_groups
    )
    me_groups = []
    for hf in his_friends:
        me_groups.append(hf)
    # groupがgroupに含まれるか,me_groupsに含まれるMessageの取得
    messages = Message.objects.filter(
        Q(group__in=groups) | Q(group__in=me_groups)
    )
    # ページネーションでページを指定
    page_item = Paginator(messages, page_num)
    return page_item.get_page(page)
