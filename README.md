# Welcome to quick-form-css

An easy-to-use fully-responsive CSS Boilerplate for your html forms.

----------
<img style="cursor: zoom-in;" src="https://github.com/siwalikm/quick-form-css/blob/master/resource/demoImg.gif?raw=true" width="100%">
This CSS boilerplate converts any simple html form into a material design minimalistic webform in 5 seconds.


> Current version 2.2.2 enables Google like input placeholder transitions
<img style="cursor: zoom-in;" src="https://raw.githubusercontent.com/siwalikm/quick-form-css/master/resource/transition.gif" width="50%">

> **Note** [Quick-Form-Css](https://github.com/siwalikm/quick-form-css) is created solely for the purpose of quick templating your html-webforms with the zero efforts. This project is a *Work-In-Progress* and might result in undesirable result at times.

----------

Themes
-------------
Quick-Form-Css comes with two themes by default, **qfc-dark** and **qfc-light**.
**qfc-dark.css**  is the theme on the left with Google forms inspired style [(url)](https://cdn.jsdelivr.net/gh/siwalikm/quick-form-css@2.2.2/qfc-dark.css),
**qfc-light.css** is the theme on the right with a more minimal look. [(url)](https://cdn.jsdelivr.net/gh/siwalikm/quick-form-css@2.2.2/qfc-light.css).

<img style="cursor: zoom-in;" src="https://github.com/siwalikm/quick-form-css/blob/master/resource/themes.jpg?raw=true">

----------

Usage
-------------

 1. In the **head section** of your html document, include the css theme you like:

>   `<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/siwalikm/quick-form-css@2.2.2/qfc-dark.css">`

or

>   `<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/siwalikm/quick-form-css@2.2.2/qfc-light.css">`

 2. In the **head section**, also add the meta viewport for the form to work correctly on handheld devices.
>   `<meta name="viewport" content="width=device-width,initial-scale=1">`

 3. Wrap your html form in a **`div`** with **`class="qfc-container"`** like this:
>   <img style="cursor: zoom-in;" src="https://github.com/siwalikm/quick-form-css/blob/master/resource/addClass.png?raw=true" width="350px">

**Awesome, you did it!**

Change Color(s)
-------------
To change theme color or background color of your form, edit the values of these css variables in your stylesheet.

    .qfc-container {
		  --form-theme-color: mediumaquamarine;
		  --form-bg-color   : white;
		  --button-hover    : gray;
		  --input-text-color: black;
     }
	 body {
    	  --main-bg-color: white;
	}

Titles and Sub-titles(s)
-------------
Quick-Form-Css supports meterial design specifications for headers from h1 to h6 [(link)](http://brm.io/material-design-type/).

All headers tags come with the default underline style. Please add class *"no-underline"* in your header element if you want to modify this behaviour.
