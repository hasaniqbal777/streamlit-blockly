import * as Blockly from 'blockly/core'
import { pythonGenerator, Order } from 'blockly/python'

Blockly.Blocks['custom_block'] = {
  init: function () {
    this.appendDummyInput().appendField('Hello World')
    this.setNextStatement(true, null)
    this.setTooltip('This is a custom block')
    this.setHelpUrl('')
    this.setColour(0)
    this.setCommentText('This is a custom block')
  },
}

pythonGenerator.forBlock['custom_block'] = function (block, generator) {
  const code = `print('Hello World')\n`
  return code
}
