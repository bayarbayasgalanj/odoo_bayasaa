/** @odoo-module **/
import SystrayMenu from 'web.SystrayMenu';
import Widget from 'web.Widget';
import rpc from 'web.rpc';

var SystrayWidget = Widget.extend({
   async willStart() {
        // if ($("#bb_news_marquee").length>0){
			rpc.query({
				model: 'bb.website.news',
				method: 'get_news',
				args: [[]],
			}).then(function (data) {
				var html = '';
				var space = '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;';
				for (var i = 0; i < data.length; i++) {
					html += data[i]+space
				}
				if (html!=''){
					$('.openerp_webclient_container').css('padding-top', '15px');
					// $('#bb_news_marquee').css(
					// 	{
					// 		display: 'none',
					// 		border: 0,
					// 		clip: rect(0 0 0 0),
					// 		height: '1px',
					// 	}
					// 	);
					$("#bb_news_marquee").find("span").html('<span>'+html+'</span>');	
					$('#bb_news_marquee').marquee({
						duration: 35000,
						pauseOnHover:true,
					});
				}
			}).finally(function (){ });
		// }
   },
});
SystrayMenu.Items.push(SystrayWidget);
export default SystrayWidget;