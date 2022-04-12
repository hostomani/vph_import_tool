odoo.define('vph_import_tool.import_tool', function (require) {
    'use strict';
    var FormController = require('web.FormController');
    var FormView = require('web.FormView');
    var FormRenderer = require('web.FormRenderer');
    var ActionManager = require('web.ActionManager');
    var viewRegistry = require('web.view_registry');
    var mvc = require('web.mvc');


    FormController.include({
        renderButtons: function($node) {
            this._super.apply(this, arguments);
            if(this.modelName == 'import.tool'){
                if (this.$buttons) {
                    let viewButtons = this.$buttons.find('.o_form_buttons_view')
                    let editButtons = this.$buttons.find('.o_form_buttons_edit')
                    viewButtons.hide()
                    editButtons.hide()
                }
            }
        },
    })
    FormRenderer.include({
        init: function(){
            this._super.apply(this, arguments)
        },
        on_attach_callback: function(){
            this._super.apply(this, arguments)
            if(this.__parentedParent.modelName == 'import.tool'){
                let cpanel = document.querySelector('.o_cp_controller')
                cpanel.style.height = '0px'
            }
        },
    })
})