function hasNetwork(online) {
    var status
    var internet_status = document.getElementById('internet_status')

    if (online){
      status = "online"
      internet_status.innerHTML = `
        <span class="btn btn-dark btn-floating btn-lg border-0"><i class="fa fa-wifi text-success"></i>
        <span>Internet restore!</span>
        </span>`
      setTimeout(function() {
        $('#internet_status').empty();
        }, 5000)

      
    }else{
      status = "offline"
      $('#internet_status').add();
      internet_status.innerHTML = `
        <span class="btn btn-dark btn-floating btn-lg border-0"><i class="fa fa-wifi text-warning"></i>
          <span> No internet connection! <br> <span class="mt-0 fs-6">Make sure you're connected to the internet</span>
          </span>
        </span>`
    }
    postInternetStatus(status);
}

function postInternetStatus(status){
    var userStatusData = {
      'status': status,
      'user': user,
      'csrfmiddlewaretoken': csrf_token,
    }

    $.ajax({
      type:'POST',
      url: login_status_url,
      data:userStatusData,
      success: function(data){
      },
      error: function(error){
      },
    });
}

function userStatus(online){

    if( user == 'AnonymousUser' || user == ''){
        
    }else{
        var status
        var login_status = document.getElementById('status')

        if (online){
            status = "online"
            login_status.classList.remove('staus_offline')
            login_status.classList.add('staus_online')              
        }else{
            status = "offline"
            login_status.classList.remove('staus_online')
            login_status.classList.add('staus_offline')
            $('#internet_status').add();
        }

        postInternetStatus(status);
    }
    
};

function postLike(){
	var like = document.getElementsByClassName('like_post');

	for (var i=0; i < like.length; i++){
		like[i].addEventListener('click', function(){
			var post_id = this.dataset.post_id
			var value = this.dataset.value
			var slug = this.dataset.slug

			//console.log('user:', user)
			if(user=='AnonymousUser'){
				//alert('login to like this post')
				var likes = $('#like');
                likes.click()				
                
			}else{
				console.log('sending data...')

				$(document).ready(function(){

					$.ajax({
						type:'POST',
						url: like_post_url,
						data:{
							post_id,
							value,
							slug,
							csrfmiddlewaretoken:(csrf_token)
						},
						success: function(data){
						},

					})

				});

			}
		})
	}
}

function postComment(){

    //comments start       

    var form = document.getElementsByClassName('comment_form')
    for (var i=0; i < form.length; i++){
        form[i].addEventListener('submit', function(e){
            e.preventDefault()
            var commentInfo;

            if (user == "AnonymousUser"){
                commentInfo = {
                    'post':this.post.value,
                    'name_comment' : this.name_comment.value,
                    'email_comment': this.email_comment.value,
                    'username_comment': this.username_comment.value,
                    'content': this.content.value,
                    'parent': this.parent.value
                }
            }else{
                commentInfo = {
                    'post':this.post.value,
                    'name_comment' : null,
                    'email_comment': null,
                    'username_comment': null,
                    'content': this.content.value,
                    'parent': this.parent.value
                }
            }
            
            submitCommentData(commentInfo);
            this.content.value = "";
            location.reload();
        })
    }

    function submitCommentData(commentInfo){

        $.ajax({
            type:'POST',                
            url: comment_post_url,
            data: {
                'comment_data':JSON.stringify(commentInfo),
                csrfmiddlewaretoken:csrf_token,
            },
            success: function(data){
                console.log(data)
            },
        })


    }

    //comments end
}

function postFollow(){
    const follow_form = document.getElementsByClassName('follow_form')
    var user_profile = document.getElementById('follow_formId').dataset.user
    var followerCount = document.getElementById('followerCount')
    var followingCount = document.getElementById('followingCount')
    var postCount = document.getElementById('postCount')
    var followbtn = document.getElementById('follow_btn')

    $(document).ready(function(){
        setInterval (function(){
            
           $.ajax({
                type:'GET',
                data: {'user_profile':user_profile},        
                url: get_followers_url,
                success: function(data){
                    followerCount.innerHTML = data['followers']
                    followingCount.innerHTML = data['following']
                    postCount.innerHTML = data['post_no']
                    followbtn.innerHTML = data['follower_value_button']
                    
                },
            }) 
        }, 2000)

    })


    
    for (var i=0; i< follow_form.length; i++){
        follow_form[i].addEventListener('submit', function(e) {
            e.preventDefault();
            follower = this.dataset.follower
            user = this.dataset.user
            value = followbtn.innerHTML

            $.ajax({
                type:'POST',                
                url: follow_url,                                        
                data:{
                    csrfmiddlewaretoken: csrf_token,
                    'follower':follower,
                    'user': user,
                    'value': value,
                },
                success: function(data){
                    console.log(data)                                                  
                },
            }) 
        })
    }
}

function detailedPost(){
    var a = document.getElementsByClassName('nodecommentform')
    for (var i=0; i < a.length; i++){
        a[i].addEventListener('submit', function(e){
                e.preventDefault()
            form = {
                'parent':this.parent.value,
                'content':this.content.value,
            }
            $.ajax({
                type:'POST',                
                url: comment_reply_url,
                data: {
                    'comment_data':JSON.stringify(form),
                    csrfmiddlewaretoken:csrf_token,
                },
                success: function(data){
                    console.log(data)
                },
            })
        }) 
    }

    var a = document.getElementsByClassName('test')
    
    var postId = []
    for (var i =0; i < a.length ; i++) {
        j =  a[i].dataset.post       
        k = {j}
        postId.push(k)
    }
    setInterval(function(){
        $.ajax({
            type:'GET',
            url: like_count_url,
            data:{
                'i':postId
            },
            success: function(data){
                
                for (var i =0; i < a.length ; i++) {
                    j =  a[i].dataset.post
                    var like = document.getElementById('likeCount'+j+'')
                    var dislike = document.getElementById('dislikeCount'+j+'')
                    var comments = document.getElementById('commentCount'+j+'')
                    like.innerHTML = data[i]['likes']
                    dislike.innerHTML = data[i]['dislikes']
                    var comment = data[i]['comments']
                    
                    comments.innerHTML = comment
                }
            },

        })
    }, 2000)  
}

function detailedBlogPost(){
    var a = document.getElementsByClassName('test')
    
    var postId = []
    for (var i =0; i < a.length ; i++) {
        j =  a[i].dataset.post       
        k = {j}
        postId.push(k)
    }
    setInterval(function(){
        $.ajax({
            type:'GET',
            url: like_count_url,
            data:{
                'i':postId
            },
            success: function(data){
                
                for (var i =0; i < a.length ; i++) {
                    j =  a[i].dataset.post
                    var like = document.getElementById('likeCount'+j+'')
                    var dislike = document.getElementById('dislikeCount'+j+'')
                    var comments = document.getElementById('commentCount'+j+'')
                    like.innerHTML = data[i]['likes']
                    dislike.innerHTML = data[i]['dislikes']
                    var comment = data[i]['comments']
                    
                    comments.innerHTML = comment
                }
            },

        })
    }, 2000) 
}

function dislay_comment_form(post){
    
    var commentForm = document.getElementById("comment"+post+"")
    if (commentForm.style.display == "none"){
        commentForm.style.display = "block"
    }else{
        commentForm.style.display = "none"
    }
}

function myfunction(id){
  var d = document.getElementById(id)
  if (d.style.display == "none"){
      d.style.display = "block"
  }else{
      d.style.display = "none"
  }                                                                                               
}
//create post view
function readURL(input){
    var reader = new FileReader();
    reader.onload = function(e) {
        $('#id_image_display')
            .attr('src', e.target.result)
    };
    reader.readAsDataURL(input.files[0]);   
}

//footer
let mybutton = document.getElementById("btn-back-to-top");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function () {
scrollFunction();
};

function scrollFunction() {
    if (
      document.body.scrollTop > 20 ||
      document.documentElement.scrollTop > 20
    ) {
      mybutton.style.display = "block";
    } else {
      mybutton.style.display = "none";
    }
}
// When the user clicks on the button, scroll to the top of the document
mybutton.addEventListener("click", backToTop);

function backToTop() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}

setTimeout(function(){
    if ($('#msg').length > 0){
        $('#msg').remove();
    }
}, 5000)

function srcToFile(src, fileName, mimeType){
    return (fetch(src)
        .then(function(res){return res.arrayBuffer();})
        .then(function(buf){return new File([buf], fileName, {type:mimeType});})
    );
}

$('.dropdownBtn').click(function(){
    $(this).children('i').toggleClass('fa-caret-right fa-caret-down')
})


/***
 * 
 * changing screen from dark mode or any initial given mode to light screen mode
 * 
 ***/
function getScreenMode() {

    if (user == 'AnonymousUser' || user == ''){
        var mode = localStorage['screen_mode']        
        if (mode =='Light'){
            initialTheme = true;
        }else{
            initialTheme = false;
        }  
        toggleColors();
    }else {
        $.ajax({
            type:'GET',
            url: screen_mode,
            success: function(data){
                var mode = data['mode']
                if (mode =='Dark'){
                    initialTheme = false;
                }else{
                    initialTheme = true;
                }  
                toggleColors();
            },
            error:function(error){
                console.log(error)
            },
        })
    }
    
}

function postScreenMode() {
    if (user == 'AnonymousUser' || user == ''){
        if (initialTheme == false){
            localStorage['screen_mode']  = 'Dark'
        }else{
            localStorage['screen_mode']  = 'Light'
        }
        toggleColors();
    }else{
        if (initialTheme == false){
            mode = 'Dark'
        }else{
            mode = 'Light'
        }

        $.ajax({
            type:'POST',
            url: screen_mode,
            data:{
                mode,
                csrfmiddlewaretoken:(csrf_token)
            },
            success: function(data){
                toggleColors();
            },
            error: function(error){
            },
        });
    }

    
}

function toggleColors() {   
    const root = document.documentElement.style;
    const darkmode = $('.darkMode-wrap')
    const s_mode = $('#s-mode')

    if(initialTheme) {

        //style btn attr
        //remove initial class list
        darkmode.children('button').children('i').removeClass('text-light')
        darkmode.children('button').removeClass('btn-dark')
        darkmode.removeClass('bg-light')
        s_mode.removeClass('text-light')
        //add new class list
        darkmode.children('button').children('i').addClass('text-dark')
        darkmode.children('button').addClass('btn-light')
        darkmode.addClass('bg-dark')
        s_mode.addClass('text-dark')

        //style var attr
        root.setProperty('--dark', 'rgb(255, 255, 255)');
        root.setProperty('--white', 'rgb(35, 35, 35)');
        root.setProperty('--lightgray1', '#616060');
        root.setProperty('--lightgray2', '#b5c3cb');
        root.setProperty('--lightgrey_phover', '#999)');
        root.setProperty('--grey', '#e5e5e5');
        document.getElementById('s-mode').innerHTML = 'Switch to dark mode'
        initialTheme = false;  
    } else {

        //style btn attr
        //remove initial class list
        darkmode.children('button').children('i').removeClass('text-dark')
        darkmode.children('button').removeClass('btn-light')
        darkmode.removeClass('bg-dark')
        s_mode.removeClass('text-dark')
        //add new class list
        darkmode.children('button').children('i').addClass('text-light')
        darkmode.children('button').addClass('btn-dark')
        darkmode.addClass('bg-light')
        s_mode.addClass('text-light')

        //style var attr
        root.setProperty('--dark', '#111');
        root.setProperty('--white', '#fff');
        root.setProperty('--lightgray1', '#f4f4f4');
        root.setProperty('--lightgray2', '#b5c3cb');
        root.setProperty('--lightgrey_phover', '#999)');
        root.setProperty('--grey', '#e5e5e5');
        document.getElementById('s-mode').innerHTML = 'Switch to light mode'
        initialTheme = true;
    }
}
