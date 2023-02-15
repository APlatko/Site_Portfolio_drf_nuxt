# Portfolio_drf_nuxt
This is my portfolio site project. It consists of backend (personal) and frontend parts (nuxt).


# Backend
Backend part (catalog "personal") is based on Django DRF framework.

    The additional applications were used:
        - ckeditor (text editor used at admin page)
        - taggit (add tags)

In models I use one-to-one and many-to-many relations. Sqlite is a default database.

For main page DefaultRouter is used to show all posts from DB and to make links for a particular post.

For authorisation JWT Token was chosen. Also implemented standard search.

All dependencies you can see at requirements.txt file.


# Frontend
Frontend part (catalog "nuxt") is based on Nuxt JS framework.

    The additional applications were used:
            - auth (standard nuxt auth module)
            - lightbox (lightbox js script for image slider)

We use default layout and layout for error page.

Navbar, footer, sidebar, and comments block is separated in Components catalogue.

Authentication is made only for making comments.


It's still need some design...