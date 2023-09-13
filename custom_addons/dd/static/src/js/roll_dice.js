odoo.define('dd.attribute_roller', function (require) {
    "use strict";

    var ajax = require('web.ajax');
    var core = require('web.core');
    var Widget = require('web.Widget');

    $(document).ready(function () {
        $('#roll-dice').click(function () {
            roll_dice();
        });
    });

    function roll_dice() {
        var attributes = [
            "character_attribute_strength_value",
            "character_attribute_dexterity_value",
            "character_attribute_constitution_value",
            "character_attribute_intelligence_value",
            "character_attribute_wisdom_value",
            "character_attribute_charisma_value"
        ];

        var defaultValues = [15, 14, 13, 12, 10, 8];
        defaultValues.sort(function () {
            return 0.5 - Math.random();
        });

        for (var i = 0; i < attributes.length; i++) {
            $('#' + attributes[i]).val(defaultValues[i]);
        }
    }
});
