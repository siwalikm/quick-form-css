# Welcome to quick-form-css
An easy-to-use fully-responsive CSS Boilerplate for your html forms. (WIP)

----------
<img style="cursor: zoom-in;" src="quickcss.gif" width="600px">

This project contains some css script which converts **any** simple html form into a nice looking minimalistic webform.

**Also you don't need to add any class or id to elements in your code for this to work.**

> **Note** [Quick-Form-Css](https://github.com/siwalikm/quick-form-css) is created solely for the purpose of quickly adding styles to raw html-webforms. Trying to use this boilerplate in webpages containing anything else might result in undesirable results.

----------

Usage
-------------

In the **head section** of your html document, include the following two lines:
>   `<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/siwalikm/quick-form-css@1.0/quick.css">`
>   `<meta name="viewport" content="width=device-width,initial-scale=1">`

**That's it.**

The link includes our **quick.css** to your project and the view port declaration is for making your form responsive on smaller devices.

Change Color(s)
-------------
To change theme or background colors of your form add the following snipped within a `<style>` tag in your head section and change the color values.

	    html {
            --main-bg-color: black;
            --form-bg-color: white;
            --form-theme-color: red;
        }
