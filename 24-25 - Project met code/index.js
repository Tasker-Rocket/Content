/**
 * This module exports a set of ESLint rules.
 * @module eslint-plugin-no-dimensions
 */
module.exports = {
    /**
     * The rules object contains all the rules for this plugin.
     * Currently, it only contains the 'no-dimensions' rule.
     */
    rules: {
        /**
         * The 'no-dimensions' rule checks for usage of Dimensions.get('window') and suggests using useWindowDimensions() instead.
         * @property {Object} 'no-dimensions' - The rule object for 'no-dimensions'.
         * @property {Function} 'no-dimensions'.create - The function to create the rule.
         * @param {Object} context - The context object provided by ESLint.
         * @returns {Object} An object containing the AST node types to listen for and the functions to run on those nodes.
         */
        'no-dimensions': {
            create: function (context) {
                return {
                    /**
                     * The MemberExpression function checks if the code matches Dimensions.get('window').
                     * @param {Object} node - The AST node to check.
                     */
                    MemberExpression(node) {
                        if (
                            node.object &&
                            node.object.type === 'CallExpression' &&
                            node.object.callee.property &&
                            node.object.callee.property.name === 'get' &&
                            node.object.callee.object.name === 'Dimensions' &&
                            node.object.arguments.length === 1 &&
                            node.object.arguments[0].type === 'Literal' &&
                            node.object.arguments[0].value === 'window'
                        ) {
                            /**
                             * If the code matches, it reports an error message.
                             */
                            context.report({
                                node: node,
                                message: 'Avoid using Dimensions.get(\'window\'). Use \'useWindowDimensions()\' instead.',
                            });
                        }
                    },
                };
            },
        },
    },
};
