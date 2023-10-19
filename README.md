# streamlit-custom-copy-buttons
Custom copy to clipboard buttons for Streamlit

The trick here is that we can’t have Javascript when we want it - however we can have javascript if we use a separate html page embedded as an iframe.

First off, you’ll need to host the copy.html file somewhere

Then, back in Streamlit we can embed an iframe using st.markdown and then using the url argument “?copy=” we have direct access to adding data to the users clipboard by pointing it to your hosted copy.html file

Now when you click on the “Copy to Clipboard” button, the text_to_copy value “Hello, World!” will be copied to your clipboard. 
There is also a 2 second transition that changes the button label so the user has some feedback that the function was activated.

This way we can pass any text we like directly to the html file using python f-strings served as an argument via url, and then any time the user clicks the button, we can add that text directly to the clipboard with Javascript via the html file.
