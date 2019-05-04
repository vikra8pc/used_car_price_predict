// Get a reference to the table body
var sel_dict ={};
var sel_list =[];
var sel_list_data='';
var tbody = d3.select("tbody");

// Console.log the weather data from data.js
// console.log(data);

// // Step 1: Loop Through `data` and console.log each weather report object
// data.forEach(function(weatherReport) {
//   console.log(weatherReport);
// });

// // Step 2:  Use d3 to append one table row `tr` for each weather report object
// // Don't worry about adding cells or text yet, just try appending the `tr` elements.
// data.forEach(function(weatherReport) {
//   console.log(weatherReport);
//   var row = tbody.append("tr");
// });

// // Step 3:  Use `Object.entries` to console.log each weather report value
// data.forEach(function(weatherReport) {
//   console.log(weatherReport);
//   var row = tbody.append("tr");

//   Object.entries(weatherReport).forEach(function([key, value]) {
//     console.log(key, value);
//   });
// });

// // Step 4: Use d3 to append 1 cell per weather report value (weekday, date, high, low)
// data.forEach(function(weatherReport) {
//   console.log(weatherReport);
//   var row = tbody.append("tr");

//   Object.entries(weatherReport).forEach(function([key, value]) {
//     console.log(key, value);
//     // Append a cell to the row for each value
//     // in the weather report object
//     var cell = tbody.append("td");
//   });
// });

// // Step 5: Use d3 to update each cell's text with
// weather report values (weekday, date, high, low)
function displaydata(new_data){
  new_data.forEach(function(weatherReport) {
  // console.log(weatherReport);
  var row = tbody.append("tr");
  
  Object.entries(weatherReport).forEach(function([key, value]) {
    // console.log(key, value);
    // Append a cell to the row for each value
    // in the weather report object
    var cell = tbody.append("td");
    cell.text(value);
  });
});
};//end displaydata

function printselectrow() {
      var submit = d3.select("#submit");
          submit.on("click", function() {

            // Prevent the page from refreshing
            d3.event.preventDefault();

            // Select the input element and get the raw HTML node
            var inputElement = d3.select("#example-form-input");

            // Get the value property of the input element
            var inputValue = inputElement.property("value");

            console.log(inputValue);

            // Set the span tag in the h1 element to the text
            // that was entered in the form
            data.forEach(function(weatherReport) {
              // console.log(weatherReport);
              
              
              Object.entries(weatherReport).forEach(function([key, value]) {
                // console.log(key, value);
                // Append a cell to the row for each value
                // in the weather report object
                if (value===inputValue){
                  
                  var body = document.querySelector('tbody');

                  while (body.firstChild) {
                  // This will remove all children within tbody which in your case are <tr> elements
                  body.removeChild(body.firstChild);
                  }
                sel_dict = weatherReport;
                sel_list.push(weatherReport);
                console.log(sel_dict)
                console.log(sel_list)
              };// end of input if
              });//end of object loop
            });// end of main data loop

            
          });//end if submit on click
          
          var tbody = d3.select("tbody");
          displaydata(sel_list);

          // $.ajax({
          //   type: 'POST',
          //   url: "./used_car_sale_price_new_data_pred.py",
          //   data: {param: sel_list}, //passing some input here
          //   dataType: "array",
          //   success: function(response){
          //      console.log(response);
          //   }
          // });

return sel_list;
}; //end of printselectrow
// displaydata(data);
var output_data=[];
output_data = printselectrow();
console.log(output_data)



// output_data.forEach(function(weatherReport) {
//   Object.entries(weatherReport).forEach(function([key, value]) {
//     // console.log(key, value);
//     var sel_list_data=`${key}:${value},`;
//   });
// });
// console.log(sel_list_data)
// d3.select("h2").text(sel_list_data);
// BONUS: Refactor to use Arrow Functions!
// data.forEach((row) => {
//   var row = tbody.append("tr");
//   Object.entries(row).forEach(([key, value]) => {
//     var cell = tbody.append("td");
//     cell.text(value);
//   });
// });
