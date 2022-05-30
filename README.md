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

### If the user is not authenticated
If the user is not authenticated, he will see the registration and authorization buttons in the right sidebar,
linking him to the corresponding pages.
#### [index.html](templates/home_page_app/index.html)
--image of the main page without authorization--
#### [login.html](templates/registration/login.html)
--image of registration--
#### [sign_up.html](templates/registration/sign_up.html)
--image of authorization--
Also on the page you can see the latest questions and find the question by name.
If you need to see the text of the question, then just click on it to go.
(About this page a little further.)
### If the user is authenticated
If the user is authenticated, then instead of the authorization and registration buttons,
he will see the buttons for going to the profile and creating a question.(More on that later.)
#### [index.html](templates/home_page_app/index.html)
--image of the main page with authorization--

## User profile page

On the profile page, the user can see his balance (cash) and the history of its changes
(up to the last 30 transactions). The sidebar contains buttons for going to the main page,
creating a question (more on that later) and logging out of the account.
#### [profile.html](templates/accounts_app/user_profile.html)
--image of user_profile--

## Create question page

On the question creation page, you can see the exit button to the menu and fields for entering
the title and content of the question (there is a check for the uniqueness of the question and 
the length of the title (9<X<31) and content (X>80)). For creating a question, the user is awarded points.
#### [create_question.html](templates/home_page_app/create_question.html)
--image of create_question--

## View question page

On the view question page, you can see the question data (Title, text, creation date, author and number of likes.),
comments (Their data is similar to the question data.), as well as a field for creating them
(There is a uniqueness check, points are awarded for creating a comment.).
You can like the question and comments (you can remove the like by pressing the button again.), this is done with ajax.
#### [view_question.html](templates/home_page_app/view_question.html)
--image of view_question--

## Admin functions



## Footer functional

In the footer, which is present on all pages of the site, you can see the current time,
the address for contacting technical support and whether the user is authorized.
(If yes, then his login will be written there.)

# Thanks



# Contacts

Poni22poni23@yandex.ru

# Licence


