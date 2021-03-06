# <img src="/README/owl-coral.png" height="50" /> Owl Nook

![Live mockup](/README/live-mockup.png)

## Table of contents

- Owl Nook
  - [Table of contents](#table-of-contents)
  - [Overview](#overview)
    - [What is this website for?](#what-is-this-website-for)
    - [What does it do?](#what-does-it-do)
    - [How does it work](#how-does-it-work)
  - [UX & UI design](#ux--ui-design)
    - [User Stories](#user-stories)
    - [Design](#design)
      - [Wireframes](#wireframes)
        - [:iphone: Mobile Wireframes](#iphone-mobile-wireframes)
        - [:iphone: Tablet Wireframes](#iphone-tablet-wireframes)
        - [:desktop_computer: Desktop Wireframes](#desktop_computer-desktop-wireframes)
      - [Colour Scheme](#colour-scheme)
      - [Typography](#typography)
      - [Imagery](#imagery)
      - [Buttons and button groups](#buttons-and-button-groups)
      - [Content Blocks](#content-blocks)
      - [Form elements](#form-elements)
      - [Other elements and reference components](#other-elements-and-reference-components)
      - [Mockups](#mockups)
      - [Interactive prototype](#interactive-prototype)
    - [Database](#database)
      - [Conceptual ERD](#conceptual-erd)
      - [Physical ERD model](#physical-erd-model)
      - [ERD Model during development](#erd-model-during-development)
    - [Existing Features](#existing-features)
      - [Common Features Across All Pages](#common-features-across-all-pages)
    - [Specific to Pages](#specific-to-pages)
    - [Features Left to Implement](#features-left-to-implement)
  - [Technologies Used](#technologies-used)
    - [Languages used](#languages-used)
    - [Frameworks, Libraries and Programs Used](#frameworks-libraries-and-programs-used)
  - [Testing](#testing)
    - [Bugs](#bugs)
    - [CSS3 validator](#css3-validator)
    - [HTML5 Validator](#html5-validator)
    - [Compatibility Testing](#compatibility-testing)
  - [Deployment](#deployment)
    - [Contribution](#contribution)
    - [Deployment to heroku](#deployment-to-heroku)
  - [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
      - [Images](#images)
    - [Dependencies + help links](#dependencies--help-links)
    - [Inspiration](#inspiration)
    - [Acknowledgements](#acknowledgements)

## Overview

### What is this website for?

The blog if for the user to find all kinds of information in one convenient place as well as share tips and funny things to the general internet.

### What does it do?

Reddit type blog full of all kinds of posts. This includes news, tips and posts just for laughs from memes to your next book to your next cocktail party type drinks. Users can posts or just browse what other people have posted. Unregistered users have very little access to content nad must join to view the entire post.

### How does it work

The website is going to be blog type layout. For those users who are there just to browse can expand on the post they are interested in but they will need to have an account to view the content. They can also save posts to read later. For those who love to share content they also need to have an account and can create posts and add photos at their own convenience. The website is built using the Django framework to handle creating user accounts and managing the website. The Postgres database is used to store general user data so that they can access their information later.

:point_right: [Live Website](https://owl-nook-dx.herokuapp.com/) :desktop_computer:

:point_right: [GitHub Repository](https://github.com/datonex/owl-nook-dx)

## UX & UI design

### User Stories

| **Role**     | **Summary**                              | **Feature**                                   |
| ------------ | ---------------------------------------- | --------------------------------------------- |
| ADMIN        | approve comments                         | filter out objectionable comments             |
| USER         | register an account                      | comment, like and view full content           |
| USER         | leave comments on a post                 | be involved in the conversion                 |
| USER         | upvote and downvote posts                | interact with content                         |
| USER         | save posts                               | access content easily at my own convenience   |
| USER         | open posts                               | read full text                                |
| USER         | view the date/time of an individual post | see which content is most up to date/ or not. |
| USER         | add categories to post                   | can get to the topics I want                  |
| USER         | filter post                              | control what content i see first              |
| USER         | follow a user                            | easily see their posts                        |
| USER / ADMIN | view the number of likes on each post    | see which is the most popular or viral        |
| USER / ADMIN | create posts                             | post blog content                             |
| USER / ADMIN | view comments on an individual posts     | read the conversation                         |
| USER / ADMIN | create draft posts                       | finish writing the content later              |

The Agile tool of choice to plan and manage my work is [Trello](https://trello.com/). The workflow is illustrated [here](https://trello.com/b/EE8FIF7B) :point_left:

### Design

#### Wireframes

Wireframes were created using [Balsamiq Wireframes](https://balsamiq.com/). The website design was inspired by the the [Medium](https://medium.com/), [Reddit](https://www.reddit.com/) and [Philosophy](https://preview.colorlib.com/#philosophy) template

The website design was based on a mobile first design and based on the features from the user stories. The website logo is to be fixed at the top right of the page and the bottom left of the footer. All register/login buttons will be in the header, fixed at the top right corner of the device.

##### :iphone: Mobile Wireframes

Click here for mobile [pdf versions](README/wireframes/mobile.pdf) :point_left:

- _Homepage_

  The homepage is meant to be simple and allows the user to view incoming posts straight away wether they are a new user or a returning user. New posts are displayed large and clearly on at the top of the page. The featured image of the blog will be large and the title with other details displayed over it. Older posts are show underneath in smaller cards with the featured image on the left content and titles on the right. The page will infinitely scroll until the first post.

  <img src="README/wireframes/img/mobile/homepage.png" height="300" />

- _Blog post_

  The blog post page will have a centered title and the user will be able to see the author of the post easily. There will be a featured image represented by the blank image and the content below it. Registered users will be able to rate and post on comments

  <img src="README/wireframes/img/mobile/blog-post.png" height="300" />

- _Category_

  Each blog post will have a category or topic that is assigned by the author of the post (category is displayed by the button under the content on blog post) When the user clicks on the button they are redirected to the category page where they will be able to view all posts in that category. Again the page will infinitely scroll.

  <img src="README/wireframes/img/mobile/category.png" height="300" />

- _About us_

  Pages that include information about Owl Nook, the legal pages and privacy pages will be based on this template.

  <img src="README/wireframes/img/mobile/about-us.png" height="300" />

- Forms: _Contact Us, Sign up, Login_

  All the forms wil be based on these templates using the appropriate for each. Ideally they will fill the entire screen and there should be no need to scroll vertically or horizontally.

  <img src="README/wireframes/img/mobile/sign-up_sign-in.png" height="300" />
  <img src="README/wireframes/img/mobile/contact-us.png" height="300" />

##### :iphone: Tablet Wireframes

Click here for tablet [pdf versions](README/wireframes/tablet.pdf) :point_left:

The tablet wireframes are very similar to the mobile wireframes with minor modifications the content and elements to fit the screen size.

<img src="README/wireframes/img/tablet/homepage.png" height="350" />
<img src="README/wireframes/img/tablet/blog-post.png" height="350" />
<img src="README/wireframes/img/tablet/category.png" height="350" />
<img src="README/wireframes/img/tablet/about-us.png" height="350" />
<img src="README/wireframes/img/tablet/sign-up_sign-in.png" height="350" />
<img src="README/wireframes/img/tablet/contact-us.png" height="350" />

##### :desktop_computer: Desktop Wireframes

Click here for Desktop [pdf versions](README/wireframes/desktop.pdf) :point_left:

The desktop wireframes are very similar to the tablet wireframes with minor modifications the content and elements to fit the screen size. The footer will be constantly displayed as the user scrolls including the categories on the right side of the page.

<img src="README/wireframes/img/desktop/homepage.png" height="300" />
<img src="README/wireframes/img/desktop/blog-post.png" height="300" />
<img src="README/wireframes/img/desktop/category.png" height="300" />
<img src="README/wireframes/img/desktop/about-us.png" height="300" />
<img src="README/wireframes/img/desktop/sign-up_sign-in.png" height="300" />
<img src="README/wireframes/img/desktop/contact-us.png" height="300" />

#### Colour Scheme

The colour scheme was generated randomly using the [coolors](https://coolors.co/ffffff-b0b7bf-0e103d-f87575) generator. I wanted it to be a dark mode theme. Initially the generator started with 5 colours but they were too many. I reduced it to three (navy, coral and grey). When I began creating the mockups, the grey did not have enough contrast with the background, particularly with small text. As a result I added white to the colour palette.

![colour palette](README/mockups/components/colour-palette.png)

The components and mockups were made using [Figma](https://www.figma.com/). The components were generated from [Creatt Studios](https://www.figma.com/@creatt) wireframe kit. When I began creating the mockups the colour scheme was more or less the same. some elements like the accent colours were quite distracting. For example the horizontal rule under the blog title. I decreased the transparency so that to help breakup text and sections but without distracting the user from reading the content. the image below will show the same colours used originally by with varying degrees of transparency reducing by 20% each time.

[![colour palette](README/mockups/components/img/colors.png)](README/mockups/components/pdf/colors.pdf)

Click here for [pdf version](README/mockups/components/pdf/colors.pdf) :point_left:

#### Typography

The font used for headings and content text is Poppins, with a backup font of sans serif. The nature of the website means that there are sections where there will be a lot of text. Poppins is a font that looks good in large and small text and, the user can also easily distinguish letters. Depending on what the user posts, wether it be italic text for quotes, or title, The entire Poppins family of fonts and font weights will be available to the user.

[![typography](README/mockups/components/img/typography.png)](README/mockups/components/pdf/typography.pdf)

Click here for [pdf version](README/mockups/components/pdf/typography.pdf) :point_left:

#### Imagery

Blog images will be posted by a user. The user must post an image when posting a blog, otherwise a default image will be used. The default image is a woman sitting typing on a laptop on a ceramic desk.

#### Buttons and button groups

Buttons and any other button groups will be based on this template below. to ensure consistent formatting when the scope of the project increases.

[![buttons](README/mockups/components/img/buttons.png)](README/mockups/components/pdf/buttons.pdf)

Click here for [pdf version](README/mockups/components/pdf/buttons.pdf) :point_left:

#### Content Blocks

Content blocks will be derived from the following template even when the scope of the project increases.

[<img src="README/mockups/components/img/content-blocks.png" height="500">](README/mockups/components/pdf/content-blocks.pdf)

Click here for [pdf version](README/mockups/components/pdf/content-blocks.pdf) :point_left:

#### Form elements

Form elements for the blog will be based in template below, This includes text input, textarea and checkboxes

[![buttons](README/mockups/components/img/form-elements.png)](README/mockups/components/pdf/form-elements.pdf)

Click here for [pdf version](README/mockups/components/pdf/form-elements.pdf) :point_left:

#### Other elements and reference components

The following items were used for reference to aid creation of components for Owl Nook website.

- [Helper Blocks](README/mockups/components/pdf/helpers.pdf) :point_left:

- [Navigation](README/mockups/components/pdf/navigation-components-dark.pdf) :point_left:

- [Shadows and other shenanigans](README/mockups/components/pdf/shadow-and-other-shenanigans.pdf) :point_left:

#### Mockups

Links will open on the Figma website and no login is required.

[Mobile wireframes](https://www.figma.com/file/XqiOnOlv4pmVabeIaTCnUr/?node-id=2%3A3) :point_left:

[Tablet wireframes](https://www.figma.com/file/XqiOnOlv4pmVabeIaTCnUr/?node-id=2%3A2) :point_left:

[Desktop wireframes](https://www.figma.com/file/XqiOnOlv4pmVabeIaTCnUr/?node-id=0%3A1) :point_left:

#### Interactive prototype

The prototypes for tablet and mobile are not shown as they are identical to the desktop prototype. To interact with the prototype, click the play button on the top right corner of the screen as shown below :point_down:

![play prototype button](README/prototype-interaction.png)

This will allow you to view the flow of the website and some of the interactions with the buttons.

[Desktop prototype](https://www.figma.com/file/DpvgBd6vfV7ZxK9vpB97pc/?node-id=0%3A1) :point_left:

### Database

#### Conceptual ERD

The database for this project began a conceptual ERD to show the relationship between each entity. Each user entity that is created either be an admin or regular member. If the user is an administrator, they have permission to add, edit or delete the category names. The normal user will only have permission to read the category and assign it to a blog post.

Each user can create a blog post entity, a comment and a reading list to save a blog post to read at their convenience.

[![conceptual ERD](README/DBMS/img/revised-conceptual-ERD.png)](README/DBMS/pdf/revised-conceptual-ERD.pdf)

Click here for [pdf version](README/DBMS/pdf/revised-conceptual-ERD.pdf) ????

#### Physical ERD model

The physical ERD model will illustrate how the entities and their information will be added to the database. I will be using crow foot notation to demonstrate the relationships.

- Each user entity has a **User_ID** attribute as the primary key. It will be used as the foreign key in blog post and whose attribute is **Author**.

- **User_ID** attribute will also be used be used as the foreign key **Member** attribute in the Comment entity.

- Each category has a **Category_ID** attribute as the primary key. It will be used as the foreign key in blog post and whose attribute is **Category**.

- Each blog post has a **Blog_Post_ID** attribute as the primary key. It will be used as the foreign key in blog post and whose attribute is **Category**.

- **Blog_Post_ID** attribute will also be used be used as the foreign key **Blog_post** attribute in the reading list entity.

[![physical ERD](README/DBMS/img/revised-ERD-crows-foot.png)](README/DBMS/pdf/revised-ERD-crows-foot.pdf)

Click here for [pdf version](README/DBMS/pdf/revised-ERD-crows-foot.pdf) ????

#### ERD Model during development

During development, The custom user model was omitted from the project to due lack of form validation. Extensive research will need to be done to be able to effectively implement this feature at a later date. For the sake of submission I opted to use the all auth user model django's model instead.

The reading list model was removed from the project and instead was implemented by adding a new bookmark field in the blog post entity.

### Existing Features

#### Common Features Across All Pages

- [x] **Links**

  - Login button for returning users is clickable and highlighted, available on buttons and are usually coral for buttons and underlined in text (dedicated button removed for mobile to conserve space)

  - All links are clickable and highlighted when hover over, with exception to user, write new blog, navbar search button and bookmark buttons for mobiles, tablets and desktops.

  - Register button for new users available on all pages (changed to get started button on mobile for mobile devices)

- [x] **Navigation bar**

  - Nav bar is consistent across all devices and pages.

  - New users can clearly make a new account from the header

  - Returning users can login into their account via button

  - Search bar is located in header for tablets and desktop devices

  - Logo is large and clear, showing the website name

  - Search bar also available via side widgets on tablets and desktops.

  - Search bar available via hamburger button for mobiles devices

- [x] **Side Widgets**

- Search widget contains search bar for user to search for post on website

- Categories widget contains current categories are are clickable to show related posts.

### Specific to Pages

- [x] **Home Page**

  - Featured post links direct to post detail page either by clicking on image or on read more button

  - Other posts when clicked direct user to its post detail page either by clicking image or read more button.

- [x] **Post Detail Page**

  - Page shows article title, author who wrote, featured image and article content

  - Next to author button there isa bookmark button for logged in user to save the post and read later

  - Author of post has 2 buttons that allows user to edit article or delete it

  - Anonymous user has book mark button disabled

  - Category badge displayed to user and is clickable to view related posts

  - Anonymous users are unable to see all post content, instead they can view a limited about and are immediately asked to log in or sign up to view the rest of the content. This

  - Anonymous user has comments and like/dislike disabled

  - Logged in user can view and add comments

- [x] **Bookmarks Page**

  - User can see their name and all the post they have saved

  - User will see that they have no posts saved if they don't have any, are prompted to go to home page to add some.

  - Clicking on image or Read more button directs user to post detail page

  - If user is not authenticated, they are redirected to login page

- [x] **Drafts Page**

  - User can see their name and all the post they have drafted

  - User will see that they have no posts saved if they don't have any, are prompted to go to home page to add some.

  - Clicking on image or Read more button directs user to edit post

  - If user is not authenticated, they are redirected to login page

- [x] **Edit Profile Page**

  - User can input optional data like enter their name and change their email

  - [x] **Edit Password Page**

  - User can change their password

- [x] **Search Page**

  - User can search for blogs by author, title or category

- [x] **Category Page**

  - All users can view posts by category

  - If user is on category travel page, the travel badge is omitted from side widget.

  - Clicking on image or Read more button directs user to post detail page

  - If Category exists, but has no posts, user is prompted to create a post via button

- [x] **Edit Post Page**

  - User can edit a draft post from their draft page with data prefilled or directly for post detail page is user is the author.

  - User can also delete post from and are prompted if they are sure via delete modal on same page.

  - If user posts a draft, they are redirected to the draft page. Otherwise is post is to be published they will be redirected to post detail page.

  - If user is not author of page, they are denied access to edit post

  - Anonymous user has no access to page

  - Anonymous user has no access

  - [x] **Add Post Page**

  - User can add a new post

  - User has option to add a category if the ones provided are not relevant to their post

  - If user posts a draft, they are redirected to the draft page. Otherwise is post is to be published they will be redirected to post detail page.

  - Anonymous user has no access

    - [x] **Add Category Page**

  - User can add a new category

  - If user posts a category they are redirected to add post page

  - Anonymous user has no access

### Features Left to Implement

- Website footer for social media links and help pages for user

- User to be able to filter posts by date or popularity.

- User profile page where user can choose their own avatar image and add a bibliography

- Author bibliography details on post detail page

- Logged in user can follow other users to later can notified if they make a new post

- Logged in user can attach multiple categories to their posts

- All users can create shareable page links to blog post to share with their friends

- When user adds a bookmark, a comment, or like a page, page update data without reloading

- User can have multiple bookmark lists and be able to name them

- Scroll to top button

- Currently the comments will show all the comments on the page, feature to load a few comments at a time

## Technologies Used

### Languages used

- [HTML](https://en.wikipedia.org/wiki/HTML5) - Add content and formatting to web page.
- [CSS](https://en.wikipedia.org/wiki/CSS) - Add styling and colours to web page.
- [JavaScript](https://www.javascript.com/) - Add interactive features to web page

- [Python](https://www.python.org/) - Used to handle user input and get data back to user.

### Frameworks, Libraries and Programs Used

- [Visual Studio Code](https://code.visualstudio.com/) - Source-code editor optimised for debugging, testing, syntax highlighting and extension support

- [Git](https://git-scm.com/) - used to allow for tracking of any changes in the code and for the version control.

- [Github](https://github.com/) - used to host the project files

- [Heroku](https://www.heroku.com/) - used to deploy web application

- [Postgres](https://postgresapp.com/) - used as the DBMS to store user profile data and hosted on Heroku

- [Balsamiq Wireframes](https://balsamiq.com/) - used to create wireframes

- [Figma](https://www.figma.com/) - used to create mockups and prototypes

- [Creatt Studios](https://www.figma.com/@creatt) - component template to illustrate mockups

- [Google Sheets](https://docs.google.com/spreadsheets/) - Tabulate user stories

- [Zapier](https://www.zapier.com/) - Automate process of adding user stories from google sheets to Trello

- [Trello](https://trello.com/) - Agile tool of choice to manage and plan web app.

- [MindNode](https://www.mindnode.com/) - app used to draw mind maps to show entities and their attributes.

- [Lucid Chart](https://www.lucidchart.com/) - web app use to illustrated database schema.

- [Canva](https://www.canva.com/) - webapp used to design logo and favicon.

- [Django](https://www.djangoproject.com/) - Python web framework to create web application and provide security to users.

- [Cloudinary](https://cloudinary.com/) - Cloud hosting service

- [Fontawesome](https://fontawesome.com/) - to insert icons in the website to make site more visually appealing and easy to navigate.

- [Favicon.io](https://favicon.io/) - used to generate favicon to webpage

- [Google Fonts](https://fonts.google.com/) - used to import 'Poppins' fonts in the style.css stylesheet.

- [TinyPNG](https://tinypng.com/) - used to reduce resolution of images

- [Bootstrap](https://getbootstrap.com/) - Used for the responsive layout as well as custom components such as image carousel, navigation bar, footer, cards, and collapse element.

- [jquery](https://jquery.com/) - Used in some of the clickable elements such as collapsible 'hamburger' nav bar and collapse element.

- [popper.js](https://popper.js.org/) - Used in some of the clickable elements such as collapsible 'hamburger' navbar and collapse element.

- [Waypoint](http://imakewebthings.com/waypoints/) - Used ad infinite scrolling function to posts

- [TinyMCE](https://www.tiny.cloud) - WYSIWYG text editor

## Testing

Automated testing was carried out using [Katalon](https://katalon.com/)

Tests can be found [here](https://github.com/datonex/owl-nook-dx/tree/master/tests) :point_left:

I used live testing and recorded the interaction. I began by testing the links on the home page as an anonymous user. Test if i am able to access restricted content: and found the following

- Limited access to post detail text. I am restricted to a few characters and prompted to login to view the rest

- Bookmark, comments and like/dislike is functionality is disabled

- Get started/login/register links direct to correct pages

- Hard coding add post page, delete article, edit article, user draft, user bookmark - I am redirected to the login page

As a registered user I attempted the same steps as as anonymous user and I attempted to access the following content

- I am able to log in to my account and I have access to article content text

- Add bookmark button is enabled

- Attempting to view empty bookmarks I am told my list is empty and prompted to add articles

- Add bookmark button is clicked on an article and is added to my list

- Like/unlike buttons update page

- Test comment post by adding content

- I have access to add posts or drafts, edit posts, add categories, delete my own posts from drafts, or article page (if I am author of page)

- I attempted to hard code add posts or drafts, edit posts, add categories, delete my own posts from drafts, or article page (if I am author of page) urls of another user. I am denied access to other user's content.

### Bugs

- [ ] Form validation fails when user logs in, attempts to change password from profile or when user creates duplicate slugs due to None type value being returned.

- [x] New categories added by user on frontend are not searchable via search bar on front end - Fixed, template did not account for empty search dictionary

- [x] Not null at category - integrity error -> Fixed-default category was not saved in database, on add post or edit post submission, if user does not set a category this error was received.

- [x] attribute error when changing status of published post to draft -> Fixed redirect lazy to home page after changing blog status, rather than returning to post detail page

- [x] Waypoints infinite scroll renders duplicate posts when paginating with class based view pagination. -> Fixed - defined pagination function and page render manually

- [x] Jquery id selector won't input html onto add post + edit post page -> Fixed - used javascript syntax

- [x] TypeError None type object being returned after comment post. No get data is being requested -> Fixed by returning previous page

- [x] HTTP404 - django attempts to input slug of a drafted post. after submission. -> Fixed - reverse lazy to post drafts page after posting blog draft

- Other bugs in trello [here](https://trello.com/b/EE8FIF7B) :point_left:

### Python Validation

python validator [Pep8](http://pep8online.com/checkresult)

#### Blog views.py

- Line break warning before operator warnings on line 272 and 273

#### Rest of python files

- Pass

### CSS3 validator

css validator [W3](https://jigsaw.w3.org/css-validator/)

#### Base css

![base css validation](README/validation/base-css.png)

- CSS Value error has now been fixed

- Warnings have not been addressed

#### Blog css

- <a href="http://jigsaw.w3.org/css-validator/check/referer">
  <img style="border:0;width:88px;height:31px"
          src="http://jigsaw.w3.org/css-validator/images/vcss-blue"
          alt="Valid CSS!" />
  </a>

  Passed validation

### HTML5 Validator

- #### Common Errors + warnings

- Type attribute warning on style element has not been fixed

- Type attribute warning on JavaScript sources element has been fixed

- Cross origin attribute error has been fixed

- `hr` element error in `ul` has been fixed

- `img` elements with no alternative text errors have been fixed

#### Home Page

![homepage html](README/validation/homepage-html.png)

- Errors above are now fixed

#### Articles Page

![articles html](README/validation/articles-html.png)

- Errors and warnings above are now fixed

#### Edit Profile Page

![edit profile html](README/validation/editprofile-html.png)

- Both CSS error not fixed, code is injected from a CDN link

- Type attribute warning on style element has not been fixed

- !DOCTYPE html value exists on page

- Rest of errors have been fixed

#### Bookmarks Page

![bookmarks html](README/validation/bookmarks-html.png)

- CSS errors not fixed, code is injected from a CDN link

- Type attribute warning on style element has not been fixed

### Compatibility Testing

- Browser Compatibility

| Screen size\Browser |       Safari       |    Opera    | Microsoft Edge |       Chrome       |      Firefox       | Internet Explorer |
| ------------------- | :----------------: | :---------: | :------------: | :----------------: | :----------------: | :---------------: |
| Mobile              | :heavy_check_mark: | Not Tested  |  Not Tested.   | :heavy_check_mark: | :heavy_check_mark: |    Not Tested     |
| Desktop             | :heavy_check_mark: | Not Tested. |  Not Tested.   | :heavy_check_mark: | :heavy_check_mark: |    Not Tested     |
| Tablet              | :heavy_check_mark: | Not Tested. |  Not Tested.   | :heavy_check_mark: | :heavy_check_mark: |    Not Tested     |

- OS Compatibility was tested on iOS 14.5.1, MacOS Catalina, iPadOS 14.5 It is yet to be tested on Unix, Linux, Windows or Solaris Operating Systems.
- The devices used in this testing include MacBook Pro, iPad Pro, iPhone 12 Pro Max, iPhone 7 Plus, Samsung Galaxy S10

- The website was exhaustively tested for responsiveness on [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools). Different viewport sizes were simulated ranging from as small as iPhone 5 (320px) to large desktop sizes (1200px and above).

## Deployment

This website was published using [Heroku](https://www.heroku.com/).

### Contribution

This website was published using [Heroku](https://heroku.com/).

1. Firstly you will need to clone this repository by running the `git clone <https://github.com/datonex/owl-nook-dx/>` command
2. If using VS Code type make sure you have th Git extension installed then type above code into your terminal
3. Navigate to project folder and start a virtual environment with `python3 -m venv .venv`
4. Activate you virtual environment with `source .venv/bin/activate`
5. Install dependencies with `pip install -r requirements.txt`
6. Make changes to the code and if you think it belongs in here then just submit a pull request

### Deployment to heroku

1. Before you begin deployment, create a git repository on github either by manually creating a repository from a template (or a new one)

2. If you have the git hub CLI installed go to the folder you keep your projects and run, `gh repo create <project-name> --public --template <template-name>` This command will automatically initialise your local repository and create your folder for you. If you don't have a template don't enter `--template`

3. Follow step 3 to 5 from contribution

4. Start a django project with `django-admin startproject <project_name> .` the a django app with `python manage.py startapp <appname>`

5. Inside project-name create a new file _env.py_ and put file name in your .gitignore

6. Open _env.py_ and type the variables:

   ```python
    import os
    # os.environ["DATABASE_URL"] = ""
    os.environ["SECRET_KEY"] = "random_secret_key"
    os.environ["HOSTNAME"] = "host_name"
    os.environ["CLOUDINARY_URL"] = "cloudinary_api_key"
    os.environ["DEVELOPMENT"] = "Development_key"
   ```

7. Locate _settings.py_ in project_name and import the following:

   ```python
   from pathlib import Path
   import os, dj_database_url

   if os.path.isfile("env.py"):
     import env
   ```

8. Set your environments variables from above where prompted byt comments:

   ```python
   SECRET_KEY = os.environ.get("SECRET_KEY")

   if "DEVELOPMENT" in os.environ:
       DEBUG = True
   else:
       DEBUG = False

   X_FRAME_OPTIONS = "SAMEORIGIN"

   ALLOWED_HOSTS = [os.environ.get("HOSTNAME")]
   ```

9. In _INSTALLED_APPS_ input the following packages installed from pip:

   ```python
   "django.contrib.messages",
   "cloudinary_storage",
   "django.contrib.staticfiles",
   "django.contrib.sites",
   "allauth",
   "allauth.account",
   "cloudinary",
   "tinymce",
   "app_name",
   ```

10. In _TEMPLATES_ inside "DIRS" build your template directories in a tuple:

    ```python
    TEMPLATES = [
      {
          "BACKEND": "django.template.backends.django.DjangoTemplates",
          "DIRS": [
              os.path.join(BASE_DIR, "templates"),
              os.path.join(BASE_DIR, "owlet", "templates", "owlet", "allauth"),
          ],
        ...
      }
    ]
    ```

11. To set up your database put in:

    ```python
    if "DATABASE_URL" in os.environ:
        DATABASES = {"default": dj_database_url.parse(os.environ.get("DATABASE_URL"))}
    else:
        DATABASES = {
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": BASE_DIR / "db.sqlite3",
            }
        }
    ```

12. Finally building the static files:

    ```python
    STATIC_URL = "owlnook-dx/static/"
    STATICFILES_STORAGE = "cloudinary_storage.storage.StaticHashedCloudinaryStorage"
    STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
    STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

    MEDIA_URL = "/media/"
    DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"
    ```

13. Create a [cloudinary](https://cloudinary.com/) account and get your API environment variable with format `CLOUDINARY_URL=cloudinary://*******************@datonex` from dashboard

14. Create a [Heroku](https://www.heroku.com/) account and login. Create a new app and select region closest to you.
    ![create app](/README/deployment/create-new-app.png)
    ![select region](/README/deployment/select-region.png)

15. From Navigation bar click on Resources.
    ![navbar](/README/deployment/navigation-heroku.png)

16. Add Heroku postgres
    ![postgresql](/README/deployment/heroku-postgres.png)

17. Sumbit the form prompt
    ![sumbit-prompt](/README/deployment/submit-form.png)

18. Commit your cahnges to github. then install the Heroku CLI (link is in Deploy from heroku navbar)

19. When Heroku CLI is installed, put in your terminal:

    ```zsh
      heroku login
    ```

    To login to Heroku

20. The connect your Git repository with: `heroku git:remote -a some-app-test` then `heroku config:set DEBUG_COLLECTSTATIC=1 --app heroku-app-name` at first deployment

21. Push your changes to heroku with `git push heroku master` or `git push heroku main`

## Credits

### Content

[Wikipedia](https://en.wikipedia.org/wiki/South_Africa#Culture) - South African culture

[Blog content sources](/README/blog-planning-spreadsheet.pdf) :point_left:
click to view content sources

### Media

#### Images

- [Placeholder image](https://www.pexels.com/photo/person-using-macbook-pro-beside-white-ceramic-mug-5052875/) - Pexels, by cottonbro

### Dependencies + help links

- [Code Institute](https://codeinstitute.net/) - Full Stack Frameworks module

- [Django-Allauth](https://github.com/pennersr/django-allauth) - Handle user sign in

- [Codemy.com](https://www.youtube.com/playlist?list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi) - crate a blog flow

- [Startbootstrap](https://startbootstrap.com/template/blog-home) - bootstrap blog template

- [Startbootstrap](https://github.com/startbootstrap/startbootstrap-blog-home) - bootstrap blog home template

- [StackOverflow](https://stackoverflow.com/questions/16014719/adding-a-jquery-script-to-the-django-admin-interface) Inject js into django admin

- [StackOverflow](https://stackoverflow.com/questions/2005822/django-forms-reload-view-after-post) - redirect user to previous page

- [Vole](https://vole.wtf/text-generator/) - random text generator

- [Techsini](https://techsini.com/multi-mockup/index.php) - Generate live mockup

- [Web fore front](https://www.webforefront.com/django/modeldatatypesandvalidation.html) - Django model data types

- [Google fonts](https://fonts.google.com/specimen/Poppins?query=poppins#standard-styles) Poppins font

- [CodingWithMitch](https://www.youtube.com/watch?v=eCeRC7E8Z7Y) - Creating a custom user model

- [Django user model](https://simpleisbetterthancomplex.com/article/2021/07/08/what-you-should-know-about-the-django-user-model.html) - information about the django user model

- [Infinite Scrolling](https://dev.to/thepylot/infinite-scroll-with-django-d0a) infinite scrolling

- [TinyMCE](https://django-tinymce.readthedocs.io/en/latest/index.html) - python package

- [Pyenchant](https://pyenchant.github.io/pyenchant/install.html) - python package to handle TinyMCE spell checker

- [Cloudinary](https://github.com/cloudinary/cloudinary-django-sample) - upload image logic

- [Change attribute names in django](https://stackoverflow.com/questions/65861544/how-do-i-change-the-name-html-attribute-of-a-django-form-field)

- [Django forms](https://docs.djangoproject.com/en/3.2/topics/forms/)

- [Django forms source code](https://docs.djangoproject.com/en/2.1/_modules/django/forms/forms/)

- [Creating form widgets](https://docs.djangoproject.com/en/4.0/ref/forms/widgets/) using Django

- [Create user forms](https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#custom-users-and-the-built-in-auth-forms)

### Inspiration

- [Medium](https://medium.com/) - Medium blog

- [Bored Pand](https://www.boredpanda.com/) - Bored Panda blog

- [Philosophy template](https://colorlib.com/wp/template/philosophy/) - wordpress website template by Colorlib

- [Philosophy template source code](https://github.com/ColorlibHQ/philosophy/blob/master/templates/404.php)

- [ERD examples](https://www.slideshare.net/ArmanHossain16/entity-relationship-diagram-for-blogging-platform)

- [ERD symbols and meanings](https://www.lucidchart.com/pages/ER-diagram-symbols-and-meaning#section_1)

- [Colorlib templates](https://colorlib.com/wp/free-bootstrap-blog-templates/)

- [Drinking blog](https://thedrinkblog.com/) - articles inspiration

- [Buzzfeed](https://www.buzzfeed.com/rheakurien/pick-a-bunch-of-beautiful-travel-destinations-and-coyaugausp) - articles inspiration

### Acknowledgements

- Thank you to my mentor for his support and guidance
