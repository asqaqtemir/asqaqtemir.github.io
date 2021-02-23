function transliter( str ) {
    
    const ru = {
        'а': 'a', 
        'б': 'b',
        'ә': 'ä',
        'і': 'ı',
        'ң': 'ŋ',
        'ғ': 'ğ',
        'ү': 'ü',
        'ұ': 'ū',
        'қ': 'q',    
        'ө': 'ö',
        'һ': 'h', 
        'й': 'i',  
        'в': 'v',
        'г': 'g', 
        'д': 'd', 
        'е': 'e', 
        'ё': 'e', 
        'ж': 'j', 
        'з': 'z', 
        'и': 'i', 
        'к': 'k', 
        'л': 'l', 
        'м': 'm', 
        'н': 'n', 
        'о': 'o', 
        'п': 'p', 
        'р': 'r', 
        'с': 's', 
        'т': 't', 
        'у': 'u', 
        'ф': 'f', 
        'х': 'h', 
        'ц': 's', 
        'ч': 'ç', 
        'ш': 'ş', 
        'щ': 'şş', 
        'ы': 'y', 
        'э': 'e', 
        'ю': 'iu', 
        'я': 'ia', ' ': ' '
    }, n_str = [];
    
    str = str.replace(/[ъь]+/g, '').replace(/й/g, 'i');
    
    for ( var i = 0; i < str.length; ++i ) {
       n_str.push(
              ru[ str[i] ]
           || ru[ str[i].toLowerCase() ] == undefined && str[i]
           || ru[ str[i].toLowerCase() ].replace(/^(.)/, function ( match ) { return match.toUpperCase() })
       );
    }
    
    return n_str.join('');
}






