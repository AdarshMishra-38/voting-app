
let  option_list = document.querySelectorAll('option')
console.log(option_list)

var counts = {};

// Iterate over the array and count occurrences of each id
data.forEach(function(obj) {
    counts[obj.choice] = (counts[obj.choice] || 0) +1;
});


for( var key in counts)
{
    for( var option of option_list)
    {
        if(option.value==key)
        {
            var span_element = option.nextElementSibling;
            console.log(span_element)
            span_element.innerText = counts[key]
          
        }
    }
}


// console.log(counts)  