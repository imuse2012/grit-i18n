#!/usr/bin/env python
# Copyright (c) 2012 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

'''Container nodes that don't have any logic.
'''


from grit.node import base
from grit.node import include
from grit.node import structure
from grit.node import message
from grit.node import io
from grit.node import misc


class GroupingNode(base.Node):
  '''Base class for all the grouping elements (<structures>, <includes>,
  <messages> and <identifiers>).'''
  def DefaultAttributes(self):
    return {
      'first_id' : '',
      'comment' : '',
      'fallback_to_english' : 'false',
      'fallback_to_low_resolution' : 'false',
    }


class IncludesNode(GroupingNode):
  '''The <includes> element.'''
  def _IsValidChild(self, child):
    return isinstance(child, (include.IncludeNode, misc.SplicingNode))


class MessagesNode(GroupingNode):
  '''The <messages> element.'''
  def _IsValidChild(self, child):
    return isinstance(child, (message.MessageNode, misc.SplicingNode))

  def ItemFormatter(self, t):
    '''Return the stringtable itemformatter if an RC is being formatted.'''
    if t in ['rc_all', 'rc_translateable', 'rc_nontranslateable']:
      from grit.format import rc  # avoid circular dep by importing here
      return rc.StringTable()
    elif t == 'c_format':
      from grit.format import c_format
      return c_format.StringTable()
    elif t == 'js_map_format':
      from grit.format import js_map_format
      return js_map_format.StringTable()
    elif t == 'chrome_messages_json':
      from grit.format import chrome_messages_json
      return chrome_messages_json.StringTable()
    elif t == 'android':
      from grit.format import android_xml
      return android_xml.ResourcesElement()


class StructuresNode(GroupingNode):
  '''The <structures> element.'''
  def _IsValidChild(self, child):
    return isinstance(child, (structure.StructureNode, misc.SplicingNode))


class TranslationsNode(base.Node):
  '''The <translations> element.'''
  def _IsValidChild(self, child):
    return isinstance(child, (io.FileNode, misc.SplicingNode))


class OutputsNode(base.Node):
  '''The <outputs> element.'''
  def _IsValidChild(self, child):
    return isinstance(child, (io.OutputNode, misc.SplicingNode))


class IdentifiersNode(GroupingNode):
  '''The <identifiers> element.'''
  def _IsValidChild(self, child):
    from grit.node import misc
    return isinstance(child, misc.IdentifierNode)
