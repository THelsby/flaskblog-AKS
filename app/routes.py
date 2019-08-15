from app import app, db, bcrypt
from flask import render_template, redirect, url_for, request
from app.models import Posts, Users
from app.forms import PostForm, RegistrationForm, LoginForm, UpdateAccountForm, UpdatePostForm
from flask_login import login_user, current_user, logout_user, login_required

@app.route('/post', methods=['GET', 'POST'])
@login_required
def post():

    form = PostForm()

    if form.validate_on_submit():
        postData = Posts(
            author=current_user,
            title=form.title.data,
            content=form.content.data
        )
        db.session.add(postData)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        print(form.errors)
    return render_template('post.html', title='Post', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():

    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data)

        user = Users(first_name=form.first_name.data,
                     last_name=form.last_name.data,
                     email=form.email.data,
                     password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('post'))
    return render_template('register.html', title="Register", form=form)


@app.route('/')
@app.route('/home')
def home():

    postData = Posts.query.all()

    return render_template('home.html', title='Home', posts=postData)


@app.route('/posts/<int:post_id>', methods=['GET', 'POST'])
def viewPost(post_id):

    postData = Posts.query.filter_by(id=post_id).first()
    form = UpdatePostForm()
    if form.validate_on_submit():
        postData.title = form.title.data
        postData.content = form.content.data

        db.session.commit()
        return redirect(url_for('viewPost', post_id=post_id))

    elif request.method == "GET":

        form.title.data = postData.title
        form.content.data = postData.content

    return render_template('postDetail.html', title='postDetail', post=postData, form=form, editPost=request.args.get('editPost'))



@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/login', methods=['GET', 'POST'])
def login():

    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()

    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()

        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)

            if request.args.get('next'):
                return redirect(request.args.get('next'))
            else:
                return redirect(url_for('home'))

    return render_template('login.html', title='Login', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/account', methods=["GET", "POST"])
@login_required
def account():
    form = UpdateAccountForm()

    if form.validate_on_submit():
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.email = form.email.data
        db.session.commit()
        return redirect(url_for('account'))

    elif request.method == "GET":
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
        form.email.data = current_user.email
    return render_template('account.html', title="Account", form=form)


