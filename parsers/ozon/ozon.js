var elements = document.getElementsByClassName('tile-hover-target i8q iq9');

let links = []

for (let el of elements){
    links.push([el.href])
}

text = await (await fetch(links[0][0]
    )).text()

var temp = document.getElementById('fuck');
temp.innerHTML = text;


function work(){
    console.log('START')
    let title = temp.getElementsByClassName('q3l')[0].innerText
    let price = temp.getElementsByClassName('lq0')[0].innerText
    let description = temp.getElementsByClassName('ra-a1')[0].innerText
    let names = temp.getElementsByClassName('yj0')
    let values = temp.getElementsByClassName('j0y')
    let seller = temp.getElementsByClassName('j8u')
    let seller_name = seller[0].innerText
    let seller_inn = seller[1].innerText
    let characteristics = []
    
    a = names.length
    for (let i=0; i<a;i++){
        characteristics.push({
            verbose_name:names[i].innerText,
            value: values[i].innerText,
            type: Number.isInteger(Number(values[i].innerText))? 'range':'category'
        })
    }
    
    let product = {
        okpd2:'Электродвигатели, генераторы и трансформаторы',
        okpd2_number: '27.11',
        title: title,
        price: price,
        description: description,
        names:names,
        values:values,
        seller:{
            name:seller_name,
            inn:seller_inn
        },
        characteristics: characteristics
    }
    
    console.log(product)    
}




setTimeout(() => work(), 10000);
