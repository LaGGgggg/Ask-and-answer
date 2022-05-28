# Ask-and-answer

it's simple, this is a site where you can ask questions and answer them. 
The project has an authorization and registration system, 
the ability to create questions and comments, like them, 
there is a user balance system (points are issued for writing questions and comments.) 
and its history, and also it is possible to administer the site through the built-in 
django admin panel. The project uses postgresql and ajax.

# How to start the project?

### 1. Clone this repository

```bash
git clone https://github.com/LaGGgggg/Ask-and-answer.git
cd Ask-and-answer
```
### 2. Install [Pipenv](https://pipenv.pypa.io/en/latest/)

### 3. Create the virtualenv

```bash
pipenv shell
```

### 4. Install python packages

```bash
pip install -r requirements.txt
```

### 5. Run database migrations

```bash
python manage.py migrate
```

### 6. Run development server

```bash
python manage.py runserver
```
# Project pages

## Main page

### If the user is authenticated
If the user is not authenticated, he will see the registration and authorization buttons
in the right sidebar, linking him to the corresponding pages.
#### [index.html](templates/home_page_app/index.html)
--image of the main page without authorization--
#### [login.html](templates/registration/login.html)
--image of registration--
#### [sign_up.html](templates/registration/sign_up.html)
--image of authorization--
Also on the page you can see the latest questions and find the question by name.
If you need to see the text of the question, then just click on it to go.
(About this page a little further.)
### If the user is not authenticated
If the user is authenticated, then instead of the authorization and registration buttons,
he will see the buttons for going to the profile and creating a question.(More on that later.)
--image of the main page with authorization--

## User profile page

On the profile page, the user can see his balance (cash) and the history of its changes
(up to the last 30 transactions). The sidebar contains buttons for going to the main page,
creating a question (more on that later) and logging out of the account.
#### [profile.html](templates/accounts_app/user_profile.html)
--image of user_profile--

## Create question page



## View question page



## Admin functions



# Thanks



# Contacts

Poni22poni23@yandex.ru

# Licence


