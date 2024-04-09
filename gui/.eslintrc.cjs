/* eslint-env node */
require('@rushstack/eslint-patch/modern-module-resolution');

module.exports = {
    root: true,
    'extends': [
        'plugin:vue/vue3-essential',
        'plugin:vue/vue3-recommended',
        'eslint:recommended',
        '@vue/eslint-config-typescript',
        '@vue/eslint-config-prettier/skip-formatting'
    ],
    parserOptions: {
        ecmaVersion: 'latest'
    },
    "plugins": [
        "@typescript-eslint",
        "vue"
    ],
    "rules": {
        "indent": [
            "warn",
            4
        ],
        "linebreak-style": [
            "off",
            "unix"
        ],
        "semi": [
            "warn",
            "always"
        ],
        "vue/max-attributes-per-line": ["warn", {
            "singleline": {
                "max": 2
            },      
            "multiline": {
                "max": 1
            }
        }],
        "vue/block-order": ["warn", {
            "order": [ [ "script", "template" ], "style" ]
        }],
        "vue/component-api-style": ["error",
            ["script-setup", "composition"]
        ],
        "vue/html-indent": ["error", 4, {
            "attribute": 1,
            "baseIndent": 1,
            "closeBracket": 0,
            "alignAttributesVertically": true,
            "ignores": []
        }],
        "vue/prefer-true-attribute-shorthand": ["warn", "always"],
        "vue/padding-line-between-tags": ["warn", [
            { "blankLine": "consistent", "prev": "*", "next": "*" }
        ]]

    }
};
