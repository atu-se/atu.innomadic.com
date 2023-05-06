# How to create HTML from Markdown in VSCode

You can preview Markdown as HTML in VSCode with no extension, but extensions will give you more powerful options.  I recommend [Markdown Preview Enhanced](https://marketplace.visualstudio.com/items?itemName=shd101wyy.markdown-preview-enhanced) and you will it for this demonstation


1. Use VSCode to create a document with an `md` extension
2. From the command palette, choose `Markdown: Markdown Preview Enhanced: Open Preview`
3. View the preview.  
4. Hold `Control` and click on the preview to bring up a context menu
5. Click `Open in browser` to immediately view in the browser
6. Alternatively, click `HTML` > `HTML (offline)` to generate an HTML file.  This should create an html file in the current folder, which you can edit or open in a browser.

## Unordered Lists

```
* You can create unordered lists with asterisks (*)
* You can create sublists using indentation
    * First
    * Second
    * Third
```

* You can create unordered lists with asterisks (*)
* You can create sublists using indentation
    * First
    * Second
    * Third

## Ordered Lists

```
You can also created ordered lists using numbers
    1. First
    2. Second
    3. Third
```

You can also created ordered lists using numbers
    1. First
    2. Second
    3. Third

## More Markdown syntax

* You can make items *italicized*
* You can make items **bold**
* Or you can format `inline code`
* You can use some HTML tags if there is not a Markdown equivalent, like `<strike>`: <strike>strike this out</strike>

```
* You can make items *italicized*
* You can make items **bold**
* Or you can format `inline code`
* You can use some HTML tags if there is not a Markdown equivalent, like `<strike>`: <strike>strike this out</strike>
```

## Headers

Create a headers of varying levels like this: 

```
# Top level header
## Second level 
### Third level
```

### This is a third level header <--

## Code blocks

To create an entire block of code, wrap place a line of "```" above and below the code

```
int x = 0
x = x + 1
```

## Code blocks 

If you specify the language, you get syntax highlighting:

```python
int x = 0;
x = x + 1
```

## ... and lots more

* You can insert images and even design tables in Markdown.
* You can clean up your Markdown syntax by running `Format Document` from the VSCode command palette.
* Other extensions will automatically generate tables or a table of contents for your document
* Your instructor uses Markdown to create HTML slideshows using Reveal.js