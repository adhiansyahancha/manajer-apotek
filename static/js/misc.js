/*
Menyimpan histori tab terakhir kali yang dipencet
Referensi: https://stackoverflow.com/a/50423867
*/
$(document).ready(function(){$('a[data-toggle="tab"]').on('show.bs.tab',function(e){localStorage.setItem('lastActiveTab',$(this).attr('href'))});var lastActiveTab=localStorage.getItem('lastActiveTab');if(lastActiveTab){$('.nav-tabs a[href="'+lastActiveTab+'"]').tab('show')}});

/**/

/*
Memperbarui jam JavaScript setiap waktu
https://stackoverflow.com/a/28415797
*/
(function(){var clockElement=document.getElementById("clock");function updateClock(clock){clock.innerHTML=new Date().toLocaleTimeString('id-ID')}setInterval(function(){updateClock(clockElement)},1000)}());