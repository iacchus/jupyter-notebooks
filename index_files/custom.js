// https://github.com/lambdalisue/jupyter-vim-binding/wiki/Customization


// DISABLE AUTOMATIC INSERTION OF MATCHING BRACES, BRACKETS, AND PARENTHESES
IPython.CodeCell.options_default.cm_config.autoCloseBrackets = false;

// SELECTING ALL
require([
  'nbextensions/vim_binding/vim_binding',
], function() {
   m_config = require("notebook/js/cell").Cell.options_default.cm_config;
   delete m_config.extraKeys['Ctrl-C'];
   CodeMirror.Vim.map("<C-a>", "ggVG", "normal");
});

// CALLING A JUPYTER SHORTCUT
// https://github.com/jupyter/notebook/blob/master/notebook/static/notebook/js/actions.js
//require(['base/js/namespace'], function(ns) {
//    ns.keyboard_manager.actions.call('jupyter-notebook:run-cell-and-insert-below');
//});
