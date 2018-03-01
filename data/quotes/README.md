# Database Quotes JSON

## JSON file with more than 5000+ famous quotes

### Below there are some examples, using jQuery, on how to work with this file

```javascript
//return array of all quotes with 12 words max
var filePath = "quotes.json";
$.getJSON(filePath).done(function (data) {
	return data.filter(function (o) {
		return o.quoteText.split(" ").length <= 12;
	});
});

//return array of all quotes of Buddha
var filePath = "quotes.json";
$.getJSON(filePath).done(function (data) {
	return data.filter(function (o) {
		return o.quoteAuthor === "Buddha";
	});
});
```
