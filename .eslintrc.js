module.exports = {
  "env": {
    "browser": true,
    "es6": true,
    "jquery": true,
    "qunit": true
  },
  "extends": "eslint:recommended",
  "globals": {
    "Atomics": "readonly",
    "SharedArrayBuffer": "readonly",

    // vendors
    "Handlebars": "readonly",
    "SelectBox": "readonly",
    "SelectFilter": "readonly",
    "TableDnD": "readonly",

    "bindBuildSelectorToProduct": "readonly",
    "bindCategorySelectorToProduct": "readonly",
    "bindComponentSelectorToProduct": "readonly",
    "bindVersionSelectorToProduct": "readonly",
    "blinddownAllCases": "readonly",
    "blindupAllCases": "readonly",
    "clearDialog": "readonly",
    "clickedSelectAll": "readonly",
    "constructForm": "readonly",
    "constructTagZone": "readonly",
    "defaultMessages": "readonly",
    "deleConfirm": "readonly",
    "fireEvent": "readonly",
    "getAjaxLoading": "readonly",
    "getBuildsByProductId": "readonly",
    "getCategoriesByProductId": "readonly",
    "getComponentsByProductId": "readonly",
    "getDialog": "readonly",
    "getRequest": "readonly",
    "getSelectedCaseIDs": "readonly",
    "getVersionsByProductId": "readonly",
    "globalCsrfToken": "readonly",
    "id_to_windowname": "readonly",
    "jQ": "readonly",
    "Nitrate": "writable",
    "popupAddAnotherWindow": "readonly",
    "postHTMLRequest": "readonly",
    "postRequest": "readonly",
    "postToURL": "readonly",
    "previewPlan": "readonly",
    "registerProductAssociatedObjectUpdaters": "readonly",
    "removeComment": "readonly",
    "renderComponentForm": "readonly",
    "sendHTMLRequest": "readonly",
    "setUpChoices": "readonly",
    "SHORT_STRING_LENGTH": "readonly",
    "splitString": "readonly",
    "submitComment": "readonly",
    "toggleExpandArrow": "readonly",
    "toggleTestCasePane": "readonly",
    "updateObject": "readonly",
  },
  "parserOptions": {
    "ecmaVersion": 2018
  },
  "rules": {
    "brace-style": ["error", "1tbs", {"allowSingleLine": true}],
    "camelcase": ["error", {"properties": "never"}],
    "curly": "error",
    "eqeqeq": "error",
    "func-style": ["error", "declaration"],
    "indent": ["error", 2, {"SwitchCase": 1}],
    "linebreak-style": ["error", "unix"],
    "no-var": "error",
    "quotes": ["error", "single", {"avoidEscape": true}],
    "object-curly-spacing": "error",
    "operator-linebreak": ["error", "after"],
    "func-call-spacing": "error",
    "no-trailing-spaces": "error",
    "space-before-function-paren": ["error", {"anonymous": "always", "named": "never", "asyncArrow": "always"}],
    "comma-spacing": "error",
    "space-infix-ops": "error",
  }
};
