# streamlit-custom-copy-buttons
Custom "Copy to Clipboard" Buttons for Streamlit


<video src="https://github.com/everydaydigital/streamlit-custom-copy-buttons/assets/12283888/9a231e14-c7b1-4f84-972f-295d64c65ad8" width="360px"></video>


Pass any text string directly to the [copy.html](copy.html) file embedded as an iframe in your Streamlit script like this:
```css
https://{your-streamlit-domain}/files/copy.html?copy={your_text_string}
```

With this method, we can add text directly to the clipboard using Javascript by clicking on an easily themeable custom button.

*Say goodbye to st.code!*
```javascript
<button id="copyButton" onclick="copyToClipboard()">Copy to Clipboard</button>
```

The trick here is that while we can’t just put Javascript anywhere we want it in Streamlit - we can still access Javascript by using a separate html page embedded as an iframe.


Start off by hosting [copy.html](copy.html) somewhere on the same domain as your streamlit script (otherwise Streamlit will block the iframe content from being embedded).

Then, create a Streamlit script like [copy.py](copy.py) to embed [copy.html](copy.html) as an iframe using st.markdown like this:
```python
###copy.py
import streamlit as st

text_to_copy = st.text_input("Hello, World!")

hosted_html_file = "https://everydayswag.org/files/copy.html"
iframe_url = f"{hosted_html_file}?copy={text_to_copy}"

st.markdown(f'<iframe src="{iframe_url}"></iframe>', unsafe_allow_html=True)
```


Now when you click on the “Copy to Clipboard” button in Streamlit, the text_to_copy value (eg “Hello, World!”) will be sent to the copy.html file via the url argument "?copy=" and copied to the the users' clipboard with Javascript.

There is also a 2 second transition that changes the button label so the user has some feedback that the function was activated.


