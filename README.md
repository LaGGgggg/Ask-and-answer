![GitHub](https://img.shields.io/github/license/LaGGgggg/Ask-and-answer?label=License%3A)
![GitHub watchers](https://img.shields.io/github/watchers/LaGGgggg/Ask-and-answer)
![GitHub last commit](https://img.shields.io/github/last-commit/LaGGgggg/Ask-and-answer)

# Ask-and-answer

It's simple, this is a site where you can ask questions and answer them. 
The project has an authorization and registration system, 
the ability to create questions and comments, like them, 
there is a user balance system (points are issued for writing questions and comments.) 
and its history, and also it is possible to administer the site through the built-in 
django admin panel. The project uses postgresql and ajax.

#### [View website>>](https://ask-and-answer-by-lagggggg.herokuapp.com/)

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

# Quickly about the functionality of the site

- Main page
  - Latest questions
  - Find the question by name
  - User is not authenticated
    - Sidebar buttons
      - Registration
      - Authorization
  - User is authenticated
    - Sidebar buttons
      - User profile
      - Create question
- User profile page
  - User balance
  - History of balance changes
    - Sidebar buttons
      - To main page
      - Create question
      - Log out
- Create question page
  - Fields
    - Title input
    - Content input
  - Sidebar buttons
    - To main page
- View question page
  - Question
    - Question data
      - Title
      - Text
      - Creation date
      - Author name
      - Number of likes
    - Like/dislike button
  - Question comments
    - Data is similar to the question data
    - Like/dislike buttons
  - Field to create a comment
    - Text input
- Superuser function
  - "To admin panel" button on each page
- Footer functional
  - Current time
  - Technical support email
  - User is authenticated
    - "Authenticated: " + username
  - User is not authenticated
    - "Not authenticated"

# Details about the functionality of the site

## Main page

### If the user is not authenticated
If the user is not authenticated, he will see the registration and authorization buttons in the right sidebar,
linking him to the corresponding pages.
#### [index.html](templates/home_page_app/index.html)
![](https://user-images.githubusercontent.com/97909133/174478166-6a094702-b391-4e35-a3da-f4df5e2121f1.png)
#### [login.html](templates/registration/login.html)
![](https://user-images.githubusercontent.com/97909133/174478197-03e9b4f4-8967-473f-92aa-c759dc0cb1a5.png)
#### [sign_up.html](templates/registration/sign_up.html)
![](https://user-images.githubusercontent.com/97909133/174478209-4e57c83d-b8da-4942-9361-41557c4b487d.png)
Also on the page you can see the latest questions and find the question by name.
If you need to see the text of the question, then just click on it to go.
(About this page a little further.)
### If the user is authenticated
If the user is authenticated, then instead of the authorization and registration buttons,
he will see the buttons for going to the profile and creating a question.(More on that later.)
#### [index.html](templates/home_page_app/index.html)
![](https://user-images.githubusercontent.com/97909133/174478232-2eb095b1-5c2c-465e-963e-3266faed79db.png)

## User profile page

On the profile page, the user can see his balance (cash) and the history of its changes
(up to the last 30 transactions). The sidebar contains buttons for going to the main page,
creating a question (more on that later) and logging out of the account.
#### [profile.html](templates/accounts_app/user_profile.html)
![](https://user-images.githubusercontent.com/97909133/174478258-0c7763a0-a515-49c8-9b01-ab5229ee4937.png)

## Create question page

On the question creation page, you can see the exit button to the menu and fields for entering
the title and content of the question (there is a check for the uniqueness of the question and 
the length of the title (9<X<31) and content (X>80)). For creating a question, the user is awarded points.
#### [create_question.html](templates/home_page_app/create_question.html)
![](https://user-images.githubusercontent.com/97909133/174478275-eb5a83e7-3e01-4925-879f-40a641d5892a.png)

## View question page

On the view question page, you can see the question data (Title, text, creation date, author name and number of likes.),
comments (Their data is similar to the question data.), as well as a field for creating them
(There is a uniqueness check, points are awarded for creating a comment.).
You can like the question and comments (you can remove the like by pressing the button again.), this is done with ajax.
(The Like button can only be seen by authorized users.)
#### [view_question.html](templates/home_page_app/view_question.html)
![](https://user-images.githubusercontent.com/97909133/174478294-0ac28c32-7995-4a70-b800-24135f166b0c.png)

## Superuser function

If you are logged in as a superuser, then on each page of the site there will be a button 
that will take you to the admin panel.
![](https://user-images.githubusercontent.com/97909133/174478317-d93c0343-49d7-4d11-8b82-830ea1e72c7b.png)
![](https://user-images.githubusercontent.com/97909133/174478327-9a5c5860-d861-48d3-9301-a6724890e83b.png)

## Footer functional

In the footer, which is present on all pages of the site, you can see the current time,
the address for contacting technical support and whether the user is authenticated.
(If yes, then his login will be written there.)

#### [View website>>](https://ask-and-answer-by-lagggggg.herokuapp.com/)
P.S. Sorry for the long loading, unfortunately after an hour of inactivity the project "falls asleep" and 
it needs more time for the first load :(.This is due to the specifics of the free Heroku that hosts the site.

# Authors

This project was done only by me, no one else helped in its creation.

# Thanks

I want to separately thank the great community,
it was thanks to them that I started and still program, thank you so much!

# Contacts

For any questions:<br>
TulNik0@yandex.ru

# License

#### [LICENSE.md](LICENSE.md)
