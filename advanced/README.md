# Internet Radio Advanced

## Basic

Look at this [file](https://github.com/Mason-Dino/Internet-Radio) for any steps before this!

## Code Environment  

All the code should be about the same from the basic. You can pick and chose which ones you want to add and don't have to choose any specific one. 

### Change Tab Name

All this code does it change the what is in the tab
```html
<!-- In the header tags -->
 <title>DSU AUDIO STREAM</title>
```

### Change order of songs
In the body add the below text

This adds a text input field within the html page

```html
<!-- This goes below the player -->
<label for="songChoice">Song Choice:</label>
<input type="text" id="songChoice" name="songChoice">
```

This adds a un-ordered list onto the html with no list items

```html
<p>Options:</p>
<ul id="songOptions">
</ul>
```

This codes goes through the number of songs that you have and makes a list item that goes in the un-ordered list.

```js
//This goes within the fetch statement from the basic

var options = document.getElementById("songOptions")
for (var i = 0; i <songs.length; i++) {
	songDisplay = "<li>" + songs[i] + "</li>"
	options.innerHTML += songDisplay
}

```

Right now we just have a text input box and list of songs or sfx that we have but the order won't change right now. The code below will change that

This makes a button within the html page that says `Submit`

```html
<button id="submit" onclick="songChange()">Submit</button>
```

This makes a function within the script tags that is able to be called within the html which is what we are doing. 

With the code it is getting the text input box contents which then is making it into an array and assigning that within `songs` variable and sets `index` back to zero to make sure it plays all songs. The it just prints out the new song list

```js
function songChange() {
	var songInput = document.getElementById("songChoice");

	songs = songInput.value.split(", ")
	index = 0;
	console.log(songs);
}
```