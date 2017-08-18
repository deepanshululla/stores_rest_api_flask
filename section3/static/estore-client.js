function httpGetAsync(theUrl, callback) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function(){
        if(xmlHttp.readyState ==4 && xmlHttp.status == 200){
            callback(xmlHttp.responseText);
        }
    }
    xmlHttp.open("GET",theUrl, true);
    // true for asynchronous
    xmlHttp.send(null);
}
httpGetAsync("https://flask-rest-api-deepanshululla.c9users.io/store",function(response){
    console.log(response);
})
httpGetAsync("https://flask-rest-api-deepanshululla.c9users.io/store/my_store",function(response){
    console.log(response);
})
httpGetAsync("https://flask-rest-api-deepanshululla.c9users.io/store/my_store/item",function(response){
    console.log(response);
})