/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component, useState } from "@odoo/owl";

export class ColorPicker extends Component {
    setup() {
        this.state = useState({
            colors: Array.from({ length: 12 }, (_, i) => i),
        });

        this.selectColor = this.selectColor.bind(this);
    }

    selectColor(color) {
        if (this.props.update) {
            this.props.update(color);
        }
    }
}

ColorPicker.template = "school.ColorPicker";

registry.category("fields").add("school_color_picker", {
    component: ColorPicker,
});