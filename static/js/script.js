const icon = document.querySelector('#button-menu');
const backgroundMenu = document.querySelector('.nav-header');
const menu = document.querySelector('.nav-header .menu');

const subMenu1 = document.querySelector('.nav-header .menu .menu-left > .item-submenu a');
const subMenu2 = document.querySelectorAll('.nav-header .menu .item-submenu2 a.title');
const btnVoltar = document.querySelectorAll('.nav-header .sub-menu li.go-back');

const imgUser = document.querySelector('.user-photo');
const subMenuUser = document.querySelector('.nav-header .menu-right .submenu-user');



// mostrando menu
$(icon).click(function(){
    if($(icon).attr('class') == 'fa fa-bars'){
        $(icon).removeClass('fa fa-bars').addClass('fa fa-times'); 
        $(menu).css({'left':'0px'});
        $(backgroundMenu).css({'width':'100%', 'background':'rgba(0,0,0,.5)'});
    }else{
        $(icon).removeClass('fa fa-times').addClass('fa fa-bars');
        $(menu).css({'left':'-320px'});
        $('.sub-menu').css({'left':'-320px'});
        $('.sub-menu2').css({'left':'-320px'});
        $(backgroundMenu).css({'width':'0%', 'background':'rgba(0,0,0,.0)'});
        
    }
});

// mostrando sub-menu
$(subMenu1).click(function(){
    $('.sub-menu').css({'left':'0px'})
});

//ocultando sub-menu
$(btnVoltar).click(function(){
    $(this).parent().css({'left':'-320px'});
});


// mostrando sub-menu2
$(subMenu2).click(function(){
    let positionMenu = $(this).parent().attr('menu');
    console.log(positionMenu);
    $('.item-submenu2[menu='+positionMenu+'] .sub-menu2').css({'left':'0px'});
});


//mostrar submenu do usuario
const atualizaSubmenu = function(){
    subMenuUser.classList.toggle('ativo');
}

imgUser.onclick = atualizaSubmenu;