(function ($) {
    
    window.DailyGreeting = Backbone.Router.extend({
        routers: {
            '': 'home'
        },

        home: function() {
            $.getJSON('greetings.json', function() {
                if (data) {
                
                } else {
                    new Error({ message: "Error loading greetings." });
                }
            });
        }
    });

})(jQuery);
