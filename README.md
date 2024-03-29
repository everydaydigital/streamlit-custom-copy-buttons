# streamlit-custom-copy-buttons
Custom "Copy to Clipboard" Buttons for Streamlit

*last tested working with: streamlit==1.28.0*

https://github.com/everydaydigital/streamlit-custom-copy-buttons/assets/12283888/4206c097-ade3-4fe6-a63d-8720f8cc56af


Pass any text string directly to the [copy.html](copy.html) file embedded as an iframe in your Streamlit script like this:
```css
https://{your-streamlit-domain}/files/copy.html?copy={your_text_string}
```

&nbsp;


With this method, we can add text directly to the clipboard using Javascript by clicking on an easily themeable custom button. 
*Say goodbye to st.code!*
```javascript
<button id="copyButton" onclick="copyToClipboard()">📋</button>
```
&nbsp;

**The trick here, is that while we can’t just put Javascript anywhere we want in Streamlit - we can still access Javascript by using a separate html page embedded as an iframe.**

&nbsp;
### Setup Instructions
1. Start off by hosting [copy.html](copy.html) somewhere on the same domain as your streamlit script (otherwise Streamlit will block the iframe content from being embedded).

2. Create a Streamlit script to embed [copy.html](copy.html) as an iframe using st.markdown like this:
  ```python
  ###copy.py
  import streamlit as st
  
  text_to_copy = st.text_input("Hello, World!")
  
  hosted_html_file = "https://everydayswag.org/files/copy.html"
  iframe_url = f"{hosted_html_file}?copy={text_to_copy}"
  
  st.markdown(f'<iframe style="overflow: hidden;" src="{iframe_url}"></iframe>', unsafe_allow_html=True)
  ```

3. Click on the “📋” button in Streamlit and the *text_to_copy* value will be loaded to the clipboard with Javascript via the url argument sent to the embedded [copy.html](copy.html) file.

&nbsp;
&nbsp;

*There is also a 1 second transition that updates the button label to "✔", giving the user some feedback that the function was activated.*
