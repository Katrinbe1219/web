
const tg=window.Telegram.WebApp
tg.expand()

const order = document.getElementById('order')
const first_page= document.getElementsByClassName('first_page')

order.addEventListener("click", () =>{
    first_page[0].style.display = 'none'
})

function loadJson(selector) {
    return JSON.parse(document.querySelector(selector).getAttribute('data-json'));
  }
window.onload = function () {
    var jsonDataMenu = loadJson('#jsonDataMenu');
  
    var menu_id = jsonDataMenu.map((item) => item.menu_id);
    var dish_id = jsonDataMenu.map((item) => item.dish_id);
    var price = jsonDataMenu.map((item) => item.price);
    var sale_id = jsonDataMenu.map((item) => item.sale_id);
    
  
    // console.log(menu_id);
    // console.log(dish_id);
    // console.log(sale_id);
    // console.log(price);

    var jsonDataDish = loadJson('#jsonDataDish');
  
    var d_id = jsonDataDish.map((item) => item.dish_id);
    var dish_name = jsonDataDish.map((item) => item.dish_name);
    var desc = jsonDataDish.map((item) => item.desc);
    var photo_tg_id = jsonDataDish.map((item) => item.photo);
  
    console.log(d_id);
    console.log(dish_name);
    console.log(desc);
    console.log(photo_tg_id);

    var jsonDataSale = loadJson('#jsonDataSale');
    
  
    var sale_num = jsonDataSale.map((item) => item.sale_id);
    var dish_id_sale = jsonDataSale.map((item) => item.dish_id);
    var sale = jsonDataSale.map((item) => item.sale);
    
    console.log(sale_num);
    console.log(dish_id_sale);
    console.log(sale);


    
}