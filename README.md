# Welcome to quick-form-css
An easy-to-use fully-responsive CSS Boilerplate for your html forms. (WIP)

----------
<img style="cursor: zoom-in;" src="https://github.com/siwalikm/quick-form-css/blob/master/resource/demo.gif?raw=true" width="100%">



This CSS boilerplate converts **any** simple html form into a material design minimalistic webform in 5 seconds.


> **Note** [Quick-Form-Css](https://github.com/siwalikm/quick-form-css) is created solely for the purpose of quick templating your html-webforms with the zero efforts. This project is a *Work-In-Progress* and might result in undesirable result at times.

----------

Themes
-------------
[Quick-Form-Css](https://github.com/siwalikm/quick-form-css) comes with two themes by default, **fw-dark** and **fw-light**.
**fw-dark.css**  is the theme on the left with Google forms inspired style [(url)](https://cdn.jsdelivr.net/gh/siwalikm/quick-form-css@2.0/fw-dark.css),
**fw-light.css** is the theme on the right with a more minimal look. [(url)](https://cdn.jsdelivr.net/gh/siwalikm/quick-form-css@2.0/fw-light.css).

<img style="cursor: zoom-in;" src="https://github.com/siwalikm/quick-form-css/blob/master/resource/themes.jpg?raw=true">

----------

Usage
-------------

 1. In the **head section** of your html document, include the css theme you like:
(using the dark theme for example)
>   `<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/siwalikm/quick-form-css@2.0/fw-dark.css">`

 2. In the **head section**, also add the meta viewport for the form to work correctly on handheld devices.
>   `<meta name="viewport" content="width=device-width,initial-scale=1">`

 3. Wrap your html form in a **`div`** with **`class="fw-container"`** like this:
>   <img style="cursor: zoom-in;" src="https://github.com/siwalikm/quick-form-css/blob/master/resource/addClass.png?raw=true" width="350px">

**Awesome, you did it!**

Change Color(s)
-------------
To change theme color or background color of your form, edit the values of these css variables in your stylesheet.

    .fw-container {
		  --form-theme-color: crimson;
		  --form-bg-color   : white;
		  --button-hover    : #4e5050; 
     }

