## Built By [Ray Ndegwa](https://github.com/sokkyyy/)

## Description
The app is a Personal Blog used to display blog posts for users to read. Users can comment on the blogs and leave their views for the Admin or other users to see.

## User Stories
These are the behaviours/features that the application implements for use by a user.

As a user I can:
* View the blog posts on the site.
* Comment on blog posts.
* View the most recent posts.
* I can join a subscription to get an email alert when a new post is made.
* See random quotes on the home page.
As an admin, I can:
* Sign in to the blog
* Create a blog post.
* Delete Comments
* Update or Delete blog posts.

## Specifications
USER:
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display blog posts starting with the latest | **On page load** | Blog posts |
| Display full blog post to read | **Click post title Link** | Redirected to a page with the blog content |
| Read comments for a post | **Scroll down on the Post page** | Form for commenting and Blog post comments|
|Update Profile Picture|**Click 'Browse' on Profile Page**|Allows logged in user to choose a new profile pic.|
ADMIN:
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| New Post | **'Post' Link on navbar** | Redirects to new post page |
| Edit Blog Post | **Click post title Link in 'admin mode'** | Redirected to a page with the form for editing a post |
| Delete a post | **Click post title Link in 'admin mode'** | Delete Button |
|Delete Comments|**Click 'delete comment'button on blog post's Page**|Deletes a blog post's comment|


## SetUp / Installation Requirements
### Prerequisites
* python3.6
* pip
* postgres database
* virtualenv

### Cloning
* In your terminal:
        
        $ git clone https://github.com/sokkyyy/personal-blog.git
        $ cd personal-blog

## Running the Application
* Creating the virtual environment:

        $ python3.6 -m venv --without-pip virtual
        $ source virtual/bin/env
        $ curl https://bootstrap.pypa.io/get-pip.py | python 

* Installing Flask and other Modules:

        $ python3.6 -m pip install Flask
        $ python3.6 -m pip install Flask-Bootstrap
        $ python3.6 -m pip install Flask-Script

* To run the application, in your terminal:

        $ chmod +x start.sh
        $ ./start.sh

### Admin 
For admin mode, register with this email:
* myemail@gmail.com


## Testing the Application
* To run the tests for the class files:

        $ python3.6 manage.py tests

## Technologies Used
* Python3.6
* Flask
* Bootstrap
* Google Fonts
* FontAwesome
* Postgres SQL

## License
[Ray Ndegwa](https://github.com/sokkyyy/)