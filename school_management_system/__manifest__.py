{
    "name": "School Management System",
    "author": "Test",
    "description": "Simple School Management System",
    "summary": "SMS",
    "category": "Education",
    "version": "0.1.0",
    "website": "test.com",
    "depends": [
        "base",
        "hr",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/student_registration_view.xml",
        "views/school_class_view.xml",
        "views/school_subject_view.xml",
        "views/school_teacher_view.xml",
        "views/school_academic_year_view.xml",
        "views/menu_items.xml",

    ],
    'assets': {
        'web.assets_backend': [
            'school_management_system/static/src/js/color_picker.js',
            'school_management_system/static/src/xml/color_picker.xml',
            'school_management_system/static/src/css/color_picker.css',
        ],
    },
    "application": True,
    "installable": True,
}
