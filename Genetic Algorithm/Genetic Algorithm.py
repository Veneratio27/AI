import random
import wx
import threading
import Queue
import math

global v_pop
v_pop = []

# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Feb 14 2017)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx.xrc

t_EVT_REFRESH = wx.NewEventType()
EVT_REFRESH = wx.PyEventBinder(t_EVT_REFRESH, 1)

q_Population = Queue.Queue()

class RefreshEvent(wx.PyCommandEvent):
    def __init__(self, etype, eid, value=None):
        wx.PyCommandEvent.__init__(self,etype,eid)
        self._value = value

    def GetValue(self):
        return self._value

class Refresh(threading.Thread):
    def __init__(self, parent,selPop=wx.NOT_FOUND,selChrome=wx.NOT_FOUND,selGene=wx.NOT_FOUND):
        threading.Thread.__init__(self)
        self._parent = parent
        self._selPop = selPop
        self._selChrome = selChrome
        self._selGene = selGene

    def run(self):
        self.populace = q_Population.get()
        self._value = [[str(len(self.populace.c)),str(len(self.populace.a))]]
        if self._selPop == 0:
            for self.i in range(len(self.populace.c)):
                self._value.append([[str(self.i),
                                    str(self.populace.c[self.i].Decode(self.populace.iset,self.populace.k)[0]),
                                    self.populace.c[self.i].Decode(self.populace.iset,self.populace.k)[1],
                                    ''.join([str(self.populace.c[self.i].g[self.j].c[self.k].v) for self.j in range(len(self.populace.c[self.i].g)) for self.k in range(len(self.populace.c[self.i].g[self.j].c))]),
                                    str(self.populace.c[self.i].f),
                                    str(self.populace.c[self.i].cr),
                                    str(self.populace.c[self.i].GeneLength)]])
                if self._selChrome != wx.NOT_FOUND:
                    for self.j in range(len(self.populace.c[self.i].g)):
                        self._value.append([[str(self.j),
                                            self.populace.c[self.i].g[self.j].Decode(self.populace.k,self.populace.rangeset),
                                            ''.join([self.populace.c[self.i].g[self.j].c[self.k].v for self.k in range(len(self.populace.c[self.i].g[self.j].c))]),
                                            str(len(self.populace.c[self.i].g[self.j].c))]])
                        if self.selGene != wxNOT_FOUND:
                            for self.k in range(len(self.populace.c[self.i].g[self.j].c)):
                                self._value.append([[str(self.k),
                                                    str(self.populace.c[self.i].g[self.j].c[self.k].v),
                                                    str(self.populace.c[self.i].g[self.j].c[self.k].cr),
                                                    str(self.populace.c[self.i].g[self.j].c[self.k].mr)]])
                                evt = RefreshEvent(t_EVT_REFRESH, -1, self._value)
                                wx.PostEvent(self._parent,evt)
                        else:
                            evt = RefreshEvent(t_EVT_REFRESH, -1, self._value)
                            wx.PostEvent(self._parent,evt)
                else:
                    evt = RefreshEvent(t_EVT_REFRESH, -1, self._value)
                    wx.PostEvent(self._parent,evt)
        elif self._selPop == 1:
            for self.i in range(len(self.populace.a)):
                self._value.append([[str(self.i),
                                    str(self.populace.c[self.i].Decode(self.populace.iset,self.populace.k)[0]),
                                    self.populace.a[self.i].Decode(self.populace.iset,self.populace.k)[1],
                                    ''.join([self.populace.a[self.i].g[self.j].c[self.k].v for self.k in range(len(self.populace.a[self.i].g[self.j].c)) for self.j in range(len(self.populace.c[self.i].g))]),
                                    str(self.populace.a[self.i].f),
                                    str(self.populace.a[self.i].cr),
                                    str(self.populace.a[self.i].GeneLength)]])
                if self._selChrome != wx.NOT_FOUND:
                    for self.j in range(len(self.populace.a[self.i].g)):
                        self._value.append([[str(self.j),
                                            self.populace.a[self.i].g[self.j].Decode(self.populace.k,self.populace.rangeset),
                                            ''.join([self.populace.a[self.i].g[self.j].c[self.k].v for self.k in range(len(self.populace.a[self.i].g[self.j].c))]),
                                            str(len(self.populace.a[self.i].g[self.j].c))]])
                        if self.selGene != wxNOT_FOUND:
                            for self.k in range(len(self.populace.a[self.i].g[self.j].c)):
                                self._value.append([[str(self.k),
                                                    str(self.populace.a[self.i].g[self.j].c[self.k].v),
                                                    str(self.populace.a[self.i].g[self.j].c[self.k].cr),
                                                    str(self.populace.a[self.i].g[self.j].c[self.k].mr)]])
                                evt = RefreshEvent(t_EVT_REFRESH, -1, self._value)
                                wx.PostEvent(self._parent,evt)
                        else:
                            evt = RefreshEvent(t_EVT_REFRESH, -1, self._value)
                            wx.PostEvent(self._parent,evt)
                else:
                    evt = RefreshEvent(t_EVT_REFRESH, -1, self._value)
                    wx.PostEvent(self._parent,evt)
        else:
            evt = RefreshEvent(t_EVT_REFRESH, -1, self._value)
            wx.PostEvent(self._parent,evt)


###########################################################################
## Class f_Viewer
###########################################################################

class f_Viewer ( wx.Frame ):
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Genetic Algorithm Viewer - ", pos = wx.DefaultPosition, size = wx.Size( 500,819 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        bs_V_Main = wx.BoxSizer( wx.VERTICAL )
        
        self.lbl_VM_Population = wx.StaticText( self, wx.ID_ANY, u"Population", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lbl_VM_Population.Wrap( -1 )
        bs_V_Main.Add( self.lbl_VM_Population, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.lct_VM_Population = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
        self.lct_VM_Population.InsertColumn(0,"Population Set")
        self.lct_VM_Population.InsertColumn(1,"Amount")
        self.lct_VM_Population.InsertStringItem(0,"General Population")
        self.lct_VM_Population.InsertStringItem(1,"Answer Population")
        bs_V_Main.Add( self.lct_VM_Population, 0, wx.ALL|wx.EXPAND, 5 )
        self.lct_VM_Population.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnPopSel)
        self.PopSel = wx.NOT_FOUND
        
        self.lbl_Chromosomes = wx.StaticText( self, wx.ID_ANY, u"Chromosomes", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lbl_Chromosomes.Wrap( -1 )
        bs_V_Main.Add( self.lbl_Chromosomes, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.lct_VM_Chromosomes = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
        self.lct_VM_Chromosomes.InsertColumn(0, "Chromosome")
        self.lct_VM_Chromosomes.InsertColumn(1, "Evaluation")
        self.lct_VM_Chromosomes.InsertColumn(2, "Equation")
        self.lct_VM_Chromosomes.InsertColumn(3, "Raw")
        self.lct_VM_Chromosomes.InsertColumn(4, "Fitness")
        self.lct_VM_Chromosomes.InsertColumn(5, "Cross Rate")
        self.lct_VM_Chromosomes.InsertColumn(6, "# of Genes")
        bs_V_Main.Add( self.lct_VM_Chromosomes, 0, wx.ALL|wx.EXPAND, 5 )
        self.lct_VM_Chromosomes.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnChromeSel)
        self.ChromeSel = wx.NOT_FOUND
        
        self.lbl_VM_Genes = wx.StaticText( self, wx.ID_ANY, u"Genes", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lbl_VM_Genes.Wrap( -1 )
        bs_V_Main.Add( self.lbl_VM_Genes, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        self.lct_VM_Genes = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
        self.lct_VM_Genes.InsertColumn(0, "Gene")
        self.lct_VM_Genes.InsertColumn(1, "Decode")
        self.lct_VM_Genes.InsertColumn(2, "Raw")
        self.lct_VM_Genes.InsertColumn(3, "Length")
        bs_V_Main.Add( self.lct_VM_Genes, 0, wx.ALL|wx.EXPAND, 5 )
        self.lct_VM_Genes.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnGeneSel)
        self.GeneSel = wx.NOT_FOUND
        
        self.lbl_VM_Codons = wx.StaticText( self, wx.ID_ANY, u"Codons", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lbl_VM_Codons.Wrap( -1 )
        bs_V_Main.Add( self.lbl_VM_Codons, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        self.lct_VM_Codons = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
        self.lct_VM_Codons.InsertColumn(0, "Codon")
        self.lct_VM_Codons.InsertColumn(1, "Value")
        self.lct_VM_Codons.InsertColumn(2, "Cross Rate")
        self.lct_VM_Codons.InsertColumn(3, "Mutation Rate")
        bs_V_Main.Add( self.lct_VM_Codons, 0, wx.ALL|wx.EXPAND, 5 )
        
        gSizer3 = wx.GridSizer( 0, 3, 0, 0 )
        
        self.btn_VM_Stop = wx.Button( self, wx.ID_ANY, u"Stop", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer3.Add( self.btn_VM_Stop, 0, wx.ALL, 5 )
        
        self.m_slider4 = wx.Slider( self, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
        gSizer3.Add( self.m_slider4, 0, wx.ALL|wx.EXPAND, 5)
        
        
        bs_V_Main.Add( gSizer3, 1, wx.EXPAND, 5 )
        
        
        self.SetSizer( bs_V_Main )
        self.Layout()
        
        self.Centre( wx.BOTH )

        self.Population = f_GAConfig.sct_CMI_Population.GetValue()
        self.InstructionSet = [f_GAConfig.lbx_CMI_Instructions.GetString(i) for i in range(f_GAConfig.lbx_CMI_Instructions.GetCount())]
        self.KeySet = [f_GAConfig.lbx_CMI_Keys.GetString(i) for i in range(f_GAConfig.lbx_CMI_Keys.GetCount())]
        self.CLengthSet = range(f_GAConfig.sct_CMI_CLength.GetValue())
        self.RangeSet = range(f_GAConfig.sct_CMI_Base.GetValue())
        self.GLength = f_GAConfig.sct_CMI_GLength.GetValue()
        self.Answer = f_GAConfig.sct_CMI_Answer.GetValue()

        self.lct_VM_Population.SetStringItem(0,1,str(self.Population))
        self.lct_VM_Population.SetStringItem(0,1,"0")

        self.qr_Population = Queue.Queue()
        self.qr_Chromosomes = Queue.Queue()
        self.qr_Genes = Queue.Queue()
        self.qr_Codons = Queue.Queue()

        self.t_pop = threading.Thread(target=Populate,args=(self.Population,self.InstructionSet,self.KeySet,self.CLengthSet,self.RangeSet,self.GLength,self.Answer))
        self.t_pop.start()
        self.Bind(EVT_REFRESH, self.OnRefresh)
        
        worker = Refresh(self, self.PopSel,self.ChromeSel, self.GeneSel)
        worker.start()

        self.Show()

    def OnPopSel(self, evt):
        self.PopSel = evt.GetIndex()
        print self.PopSel

    def OnChromeSel(self, evt):
        self.ChromeSel = evt.GetIndex()

    def OnGeneSel(self, evt):
        self.GeneSel = evt.GetIndex()

    def OnRefresh(self, evt):
        self.val = evt.GetValue()
        wx.MessageBox(str(self.val), 'Info',  wx.OK | wx.ICON_INFORMATION)
        for self.i in range(len(self.val)):
            wx.MessageBox('First For i = ' + str(self.i), 'Info',  wx.OK | wx.ICON_INFORMATION)
            for self.j in range(len(self.val[self.i])):
                wx.MessageBox('First For i = ' + str(self.i) + ' j = ' + str(self.j), 'Info',  wx.OK | wx.ICON_INFORMATION)
                if self.i == 0:
                    self.lct_VM_Population.SetStringItem(self.j,1,self.val[self.i][self.j])
                elif self.i == 1:
                    wx.MessageBox('1', 'Info',  wx.OK | wx.ICON_INFORMATION)
                    for self.k in range(len(self.val[self.i][self.j])):
                        if int(self.val[self.i][self.j][0]) > self.lct_VM_Chromosomes.GetItemCount()-1:
                            self.lct_VM_Chromosomes.InsertStringItem(self.j,self.val[self.i][self.j][self.k])
                        else:
                            self.lct_VM_Chromosomes.SetStringItem(self.j,self.k,self.val[self.i][self.j][self.k])
                elif self.i == 2:
                    wx.MessageBox('2', 'Info',  wx.OK | wx.ICON_INFORMATION)
                    for self.k in range(len(self.val[self.i][self.j])):
                        if int(self.val[self.i][self.j][0]) > self.lct_VM_Genes.GetItemCount()-1:
                            self.lct_VM_Genes.InsertStringItem(self.j,self.val[self.i][self.j][self.k])
                        else:
                            self.lct_VM_Genes.SetStringItem(self.j,self.k,self.val[self.i][self.j][self.k])
                elif self.i == 3:
                    wx.MessageBox('3', 'Info',  wx.OK | wx.ICON_INFORMATION)
                    for self.k in range(len(self.val[self.i][self.j])):
                        if int(self.val[self.i][self.j][0]) > self.lct_VM_Codons.GetItemCount()-1:
                            self.lct_VM_Codons.InsertStringItem(self.j,self.val[self.i][self.j][self.k])
                        else:
                            self.lct_VM_Codons.SetStringItem(self.j,self.k,self.val[self.i][self.j][self.k])
        wx.MessageBox('After First For', 'Info',  wx.OK | wx.ICON_INFORMATION)
        if self.PopSel != wx.NOT_FOUND:
            for self.i in range(1,len(self.val)):
                if self.i == 1:
                    for self.j in range(len(self.val[self.i]), self.lct_VM_Chromosomes.GetItemCount()):
                        self.lct_VM_Chromosomes.DeleteItem(self.j)
                elif self.i == 2:
                    for self.j in range(len(self.val[self.i]), self.lct_VM_Genes.GetItemCount()):
                        self.lct_VM_Genes.DeleteItem(self.j)
                elif self.i == 3:
                    for self.j in range(len(self.val[self.i]), self.lct_VM_Codons.GetItemCount()):
                        self.lct_VM_Codons.DeleteItem(self.j)
            for self.i in range(len(self.val),4):
                if self.i == 2:
                    self.lct_VM_Genes.DeleteAllItems()
                elif self.i == 3:
                    self.lct_VM_Codons.DeleteAllItems()
        else:
            self.lct_VM_Chromosomes.DeleteAllItems()
            self.lct_VM_Genes.DeleteAllItems()
            self.lct_VM_Codons.DeleteAllItems()
        wx.MessageBox('After Last For', 'Info',  wx.OK | wx.ICON_INFORMATION)
        self.lct_VM_Population.SetItemState(0,wx.LIST_STATE_SELECTED, wx.LIST_STATE_SELECTED)
        worker = Refresh(self, self.PopSel,self.ChromeSel, self.GeneSel)
        worker.start()
        
    def __del__( self ):
        pass


###########################################################################
## Class f_Config
###########################################################################

class f_Config ( wx.Frame ):
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Genetic Algorithm Configuration", pos = wx.DefaultPosition, size = wx.Size( 315,559 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        bs_C_Main = wx.BoxSizer( wx.VERTICAL )
        
        fgs_CM_Input = wx.FlexGridSizer( 0, 2, 0, 0 )
        fgs_CM_Input.SetFlexibleDirection( wx.BOTH )
        fgs_CM_Input.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.lbl_CMI_Population = wx.StaticText( self, wx.ID_ANY, u"Population", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lbl_CMI_Population.Wrap( -1 )
        fgs_CM_Input.Add( self.lbl_CMI_Population, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        self.sct_CMI_Population = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 1000000000, 0 )
        fgs_CM_Input.Add( self.sct_CMI_Population, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.lbl_CMI_Library = wx.StaticText( self, wx.ID_ANY, u"Instruction Library", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lbl_CMI_Library.Wrap( -1 )
        fgs_CM_Input.Add( self.lbl_CMI_Library, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        lbx_CMI_LibraryChoices = ["isint(self.gval)","isoperator(self.gval)"]
        self.lbx_CMI_Library = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, lbx_CMI_LibraryChoices, 0 )
        fgs_CM_Input.Add( self.lbx_CMI_Library, 0, wx.ALL|wx.EXPAND, 5 )
        self.lbx_CMI_Library.Bind(wx.EVT_LISTBOX, self.LibSel)
        
        self.btn_CMI_Add = wx.Button( self, wx.ID_ANY, u"Add", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgs_CM_Input.Add( self.btn_CMI_Add, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
        self.btn_CMI_Add.Bind(wx.EVT_BUTTON, self.AddInstruction)
        self.btn_CMI_Add.Enable(False)
        
        self.btn_CMI_Remove = wx.Button( self, wx.ID_ANY, u"Remove", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgs_CM_Input.Add( self.btn_CMI_Remove, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
        self.btn_CMI_Remove.Bind(wx.EVT_BUTTON, self.RemoveInstruction)
        self.btn_CMI_Remove.Enable(False)
        
        self.lbl_CMI_Instructions = wx.StaticText( self, wx.ID_ANY, u"Instruction Set", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lbl_CMI_Instructions.Wrap( -1 )
        fgs_CM_Input.Add( self.lbl_CMI_Instructions, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        lbx_CMI_InstructionsChoices = []
        lbx_CMI_InstructionsChoices = lbx_CMI_LibraryChoices
        self.lbx_CMI_Instructions = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, lbx_CMI_InstructionsChoices, 0 )
        fgs_CM_Input.Add( self.lbx_CMI_Instructions, 0, wx.ALL|wx.EXPAND, 5 )
        self.lbx_CMI_Instructions.Bind(wx.EVT_LISTBOX, self.InsSel)
        
        self.lbl_CMI_Keys = wx.StaticText( self, wx.ID_ANY, u"Key Set\nRight-Click for Menu", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
        self.lbl_CMI_Keys.Wrap( -1 )
        fgs_CM_Input.Add( self.lbl_CMI_Keys, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        lbx_CMI_KeysChoices = []
        lbx_CMI_KeysChoices = ['0','1','2','3','4','5','6','7','8','9','+','-','*','/']
        self.lbx_CMI_Keys = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, lbx_CMI_KeysChoices, 0 )
        fgs_CM_Input.Add( self.lbx_CMI_Keys, 0, wx.ALL|wx.EXPAND, 5 )
        self.lbx_CMI_Keys.Bind(wx.EVT_RIGHT_DOWN, self.ContextKeys)
        
        self.lbl_CMI_CLength = wx.StaticText( self, wx.ID_ANY, u"Max Chromosome Length", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lbl_CMI_CLength.Wrap( -1 )
        fgs_CM_Input.Add( self.lbl_CMI_CLength, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        self.sct_CMI_CLength = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
        fgs_CM_Input.Add( self.sct_CMI_CLength, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.lbl_CMI_Base = wx.StaticText( self, wx.ID_ANY, u"Base Value for Codons", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lbl_CMI_Base.Wrap( -1 )
        fgs_CM_Input.Add( self.lbl_CMI_Base, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        self.sct_CMI_Base = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
        fgs_CM_Input.Add( self.sct_CMI_Base, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.lbl_CMI_GLength = wx.StaticText( self, wx.ID_ANY, u"Gene Length", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lbl_CMI_GLength.Wrap( -1 )
        fgs_CM_Input.Add( self.lbl_CMI_GLength, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        self.sct_CMI_GLength = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
        fgs_CM_Input.Add( self.sct_CMI_GLength, 0, wx.ALL|wx.EXPAND, 5 )

        self.lbl_CMI_Answer = wx.StaticText( self, wx.ID_ANY, u"Answer", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
        self.lbl_CMI_Answer.Wrap( -1 )
        fgs_CM_Input.Add( self.lbl_CMI_Answer, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        self.sct_CMI_Answer = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 1000000000, 0 )
        fgs_CM_Input.Add( self.sct_CMI_Answer, 0, wx.ALL|wx.EXPAND, 5 )
        
        
        bs_C_Main.Add( fgs_CM_Input, 1, wx.EXPAND, 5 )
        
        self.btn_CM_Start = wx.Button( self, wx.ID_ANY, u"Start", wx.DefaultPosition, wx.DefaultSize, 0 )
        bs_C_Main.Add( self.btn_CM_Start, 0, wx.ALL|wx.EXPAND, 5 )
        self.btn_CM_Start.Bind(wx.EVT_BUTTON, self.OnStart)

        self.lbl_CM_Require = wx.StaticText( self, wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lbl_CM_Require.Wrap( -1 )
        bs_C_Main.Add( self.lbl_CM_Require, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        self.SetSizer( bs_C_Main )
        self.Layout()
        
        self.Centre( wx.BOTH )

        self.sct_CMI_Population.SetValue(1000)
        self.sct_CMI_CLength.SetValue(10)
        self.sct_CMI_Base.SetValue(2)
        self.sct_CMI_GLength.SetValue(4)
        self.sct_CMI_Answer.SetValue(24)

    def ContextKeys(self, event):
        menu = ContextKeys(self)
        self.PopupMenu(menu, event.GetPosition()+self.lbx_CMI_Keys.Position)
        menu.Destroy()

    def AddInstruction(self, event):
        self.lbx_CMI_Instructions.Append(self.lbx_CMI_Library.GetString(self.lbx_CMI_Library.GetSelection()))
        self.lbx_CMI_Library.SetSelection(-1)
        self.btn_CMI_Add.Enable(False)

    def RemoveInstruction(self, event):
        self.lbx_CMI_Instructions.Delete(self.lbx_CMI_Instructions.GetSelection())
        self.lbx_CMI_Instructions.SetSelection(-1)
        self.btn_CMI_Remove.Enable(False)
                                        

    def LibSel(self, event):
        self.btn_CMI_Add.Enable(True)

    def InsSel(self, event):
        self.btn_CMI_Remove.Enable(True)

    def OnStart(self, event):
        if self.sct_CMI_Population.GetLabel() == 0:
            self.lbl_CM_Require.SetLabelText("Population cannot be 0")
            return
        if self.lbx_CMI_Instructions.GetCount() == 0:
            self.lbl_CMI_Require.SetLabelText("Please add Instructions from the Library")
            return
        if self.lbx_CMI_Keys.GetCount() == 0:
            self.lbl_CMI_Require.SetLabelText("Must have at least one key")
            return
        if self.sct_CMI_CLength.GetValue() == 0:
            self.lbl_CMI_Require.SetLabelText("Chromosome Length cannot be 0")
            return
        if self.sct_CMI_Base.GetValue() == 0:
            self.lbl_CMI_Require.SetLabelText("Base value cannot be 0")
            return
        if self.sct_CMI_GLength.GetValue() == 0:
            self.lbl_CMI_Require.SetLabelText("Gene Length cannot be 0")
            return
        v_pop.append(f_Viewer(self))
    
    def __del__( self ):
        pass


class ContextKeys(wx.Menu):
    def __init__(self, WinName):
        wx.Menu.__init__(self)

        self.WinName = WinName
 
        item = wx.MenuItem(self, wx.NewId(), "Add")
        self.AppendItem(item)
        self.Bind(wx.EVT_MENU, self.OnAdd, item)
     
        item = wx.MenuItem(self, wx.NewId(),"Delete")
        self.AppendItem(item)
        self.Bind(wx.EVT_MENU, self.OnDelete, item)
        if self.WinName.lbx_CMI_Keys.GetSelection() == wx.NOT_FOUND : item.Enable(False)
     
        item = wx.MenuItem(self, wx.NewId(),"Clear")
        self.AppendItem(item)
        self.Bind(wx.EVT_MENU, self.OnClear, item)

        item = wx.MenuItem(self, wx.NewId(),"Edit")
        self.AppendItem(item)
        self.Bind(wx.EVT_MENU, self.OnEdit, item)
        if self.WinName.lbx_CMI_Keys.GetSelection() == wx.NOT_FOUND : item.Enable(False) 

        item = wx.MenuItem(self, wx.NewId(),"Move Up")
        self.AppendItem(item)
        self.Bind(wx.EVT_MENU, self.OnMoveUp, item)
        if self.WinName.lbx_CMI_Keys.GetSelection() == wx.NOT_FOUND : item.Enable(False) 

        item = wx.MenuItem(self, wx.NewId(),"Move Down")
        self.AppendItem(item)
        self.Bind(wx.EVT_MENU, self.OnMoveDown, item)
        if self.WinName.lbx_CMI_Keys.GetSelection() == wx.NOT_FOUND : item.Enable(False) 

        item = wx.MenuItem(self, wx.NewId(),"Clear Selection")
        self.AppendItem(item)
        self.Bind(wx.EVT_MENU, self.OnClearSel, item)
        if self.WinName.lbx_CMI_Keys.GetSelection() == wx.NOT_FOUND : item.Enable(False) 
 
    def OnAdd(self, event):
        dlg = wx.TextEntryDialog(self.WinName, "Enter the value you would like to add to the Key Set", "Add to Key Set")
        if dlg.ShowModal() == wx.ID_OK:
            sel = self.WinName.lbx_CMI_Keys.GetSelection()
            if sel == wx.NOT_FOUND:
                self.WinName.lbx_CMI_Keys.Append(dlg.GetValue())
            else:
                self.WinName.lbx_CMI_Keys.InsertItems([dlg.GetValue()],sel)
        dlg.Destroy()
 
    def OnDelete(self, event):
        sel = self.WinName.lbx_CMI_Keys.GetSelection()
        if sel != wx.NOT_FOUND:
            self.WinName.lbx_CMI_Keys.Delete(sel)

    def OnClear(self, event):
        self.WinName.lbx_CMI_Keys.Clear()

    def OnEdit(self, event):
        sel = self.WinName.lbx_CMI_Keys.GetSelection()
        if sel != wx.NOT_FOUND:
            dlg = wx.TextEntryDialog(self.WinName, "Enter the value you would like to add to the Key Set", "Add to Key Set")
            if dlg.ShowModal() == wx.ID_OK:
                self.WinName.lbx_CMI_Keys.SetString(sel, dlg.GetValue())
            dlg.Destroy()

    def OnMoveUp(self, event):
        sel = self.WinName.lbx_CMI_Keys.GetSelection()
        if sel != wx.NOT_FOUND:
            if sel != 0:
                Temp = self.WinName.lbx_CMI_Keys.GetString(sel)
                self.WinName.lbx_CMI_Keys.SetString(sel, self.WinName.lbx_CMI_Keys.GetString(sel-1))
                self.WinName.lbx_CMI_Keys.SetString(sel-1, Temp)

    def OnMoveDown(self, event):
        sel = self.WinName.lbx_CMI_Keys.GetSelection()
        if sel != wx.NOT_FOUND:
            if sel != self.WinName.lbx_CMI_Keys.GetCount() - 1:
                Temp = self.WinName.lbx_CMI_Keys.GetString(sel)
                self.WinName.lbx_CMI_Keys.SetString(sel, self.WinName.lbx_CMI_Keys.GetString(sel+1))
                self.WinName.lbx_CMI_Keys.SetString(sel+1, Temp)

    def OnClearSel(self, event):
        self.WinName.lbx_CMI_Keys.SetSelection(-1)

def isoperator(value):
    if value.isdigit() == False:
        for i in ["+","-","*","/"]:
            if value == i:
                return True
        return False
    else:
        return False

def isint(value):
    try:
        int(value)
        return True
    except:
        return False

class Codon():
    def __init__(self, value, crossover):
        self.mr = 0.001
        self.v = value
        self.cr = crossover

class Gene():
    def __init__(self, rangeset, length, crossrate):
        self.glength = length
        self.c = []
        for self.i in range(length):
            self.c.append(Codon(random.choice(rangeset), crossrate))

    def Decode(self, key, rangeset):
        self.index = 0
        for self.i in range(len(self.c)):
            self.index = self.index + self.c[self.i].v*len(rangeset)**(len(self.c)-self.i-1)
        if self.index >= len(key):
            return ""
        else:
            return key[self.index]

class Chromosome():
    def __init__(self,parent, length, rangeset, glength, fitness):
        self.r = rangeset
        self.cr = 0.3
        self.f = fitness
        self.GeneLength = glength
        self.g = []
        self.value = 0
        self.parent = parent
        for i in range(length):
            self.g.append(Gene(self.r, glength, self.cr/(float(length)*float(glength))))
        

    def Decode(self, instructionset, key):
        self.val = []
        self.j = 0
        for self.i in range(len(self.g)):
            self.gval = self.g[self.i].Decode(key,self.r)
            self.check = eval(instructionset[self.j%len(instructionset)])
            if self.check:
                self.val.append(self.gval)
                self.j = self.j+1
        if len(self.val) != 0:
            self.val = ''.join(self.val)
            if self.val != "":
                try:
                    return [eval(self.val),self.val]
                except:
                    return ["",""]
            else:
                return [self.val,self.val]
        else:
            return ["",""]

    def totallen(self):
        self.val = 0
        for self.i in range(len(self.g)):
            self.val = self.val + len(self.g[self.i].c)
        return self.val

    def split(self, Index):
        self.newGene = Gene([0,1],self.totallen()-Index,0.1)
        for self.i in range(Index, self.totallen()):
            print self.outputData(self.parent.iset,self.parent.k)
            print self.i
            print Index
            print len(self.g)
            print Index
            print Index/len(self.g)
            print math.floor(Index/len(self.g))
            print int(math.floor(Index/len(self.g)))
            print self.g[int(math.floor(Index/len(self.g)))].c
            print len(self.g[int(math.floor(Index/len(self.g)))].c)
            print self.g[int(math.floor(Index/len(self.g)))].c[Index%len(self.g[int(math.floor(Index/len(self.g)))].c)]
            self.newGene.c[self.i-Index] = self.g[int(math.floor(Index/len(self.g)))].c.pop(Index%len(self.g[int(math.floor(Index/len(self.g)))].c))
        for self.i in range(len(self.g)):
            print self.outputData(self.parent.iset,self.parent.k)
            print self.i
            print len(self.g)
            print Index
            print Index/len(self.g)
            if self.i >= Index/len(self.g):
                self.g.pop(self.i)
        return self.newGene

    def append(self, newGene):
        bnone = True
        for self.i in range(len(self.g)):
            if self.g[self.i].glength > len(self.g[self.i].c):
                bnone = False
                break
        if bnone == False:
            for self.i in range(len(self.g[self.i].c),self.g[self.i].glength):
                self.g[self.i].c.append(newGene.c.pop(0))
        self.Temp = Gene([0,1], self.GeneLength, 0.1)
        while len(newGene.c) > 0:
            if len(newGene.c) >= len(self.Temp.c):
                for self.i in range(len(self.Temp.c)):
                    self.Temp.c[self.i] = newGene.c.pop(0)
            else:
                self.Temp = newGene
            self.g.append(self.Temp)

    def reEvalCR(self):
        self.cr = 0
        for self.i in self.g:
            for self.j in self.i.c:
                self.cr += self.j.cr

    def outputData(self, InstSet, Key):
        self.Temp = self.Decode(InstSet, Key)
        return '\n'.join(["Total Length - " + str(self.totallen()),
                         "Fitness Value" + str(self.f),
                         "Decoded Information - " + str(self.Temp),
                         "Binary Data - " + ''.join([str(self.j.v) for self.i in self.g for self.j in self.i.c]),
                         "Length of the Genes - " + str(self.GeneLength),
                         "Amount of Genes - " + str(len(self.g)),
                         "Codon Data",
                         "Value, Cross Rate, Mutation Rate",
                         '\n'.join([','.join([str(self.k) for self.k in [self.j.v,self.j.cr,self.j.mr]]) for self.i in self.g for self.j in self.i.c])])

class Populate():
    def __init__(self, population, instructionset, key, lengthrange, rangeset, glength, Answer):
        self.p = population
        self.iset = instructionset
        self.k = key
        self.rangeset = rangeset
        self.c = []
        self.a = []
        self.Answer = Answer
        for i in range(self.p):
            self.c.append(Chromosome(self,random.choice(lengthrange),rangeset,glength,1/float(self.p)))
        oldpop = self.p
        for i in range(self.p):
            self.Decode(i-(oldpop-self.p))
        q_Population.put(self)
        self.Genetics()
            
    def Decode(self, ichromosome):
        self.value = self.c[ichromosome].Decode(self.iset, self.k)
        self.equation = self.value[1]
        self.value = self.value[0]
        if self.value != "":
            if self.value == self.Answer:
                self.a.append(self.c.pop(ichromosome))
                self.p = self.p - 1
                print self.equation
                if self.p%50 == 0 : print "Chromosomes Remaining - " + str(self.p)
            else:
                self.c[ichromosome].f = 1/(abs(float(self.Answer)-float(self.value)))
            self.c[ichromosome].value = self.value
            return self.value
        else:
            self.c.pop(ichromosome)
            self.p = self.p - 1
            if self.p%50 == 0 : print "Chromosomes Remaining - " + str(self.p)

    def Genetics(self):
        while self.p > 1:
            self.populace = []
            #print "Genetics - populate for Choice1"
            for self.i in range(self.p):
                for self.j in range(int(self.p*self.c[self.i].f)):
                        try:
                            self.populace.append(self.i)
                        except:
                            print '\n'.join(['\n'.join(["Chromosome " + str(self.j),self.c[self.j].outputData(self.iset, self.k),""]) for self.j in range(self.p)])
            #print len(self.populace)
            #print self.p
            self.choice1 = random.choice(self.populace)
            self.c[self.choice1].f = 1/float(self.p)
            self.populace = []
            #print "Genetics - populate for Choice2"
            for self.i in range(self.p):
                if self.i != self.choice1:
                    for self.j in range(int(self.p*self.c[self.i].f)):
                        self.populace.append(self.i)
            #print len(self.populace)
            self.choice2 = random.choice(self.populace)
            self.c[self.choice2].f = 1/float(self.p)
            self.populace = []
            self.length1 = 0
            self.length2 = 0
            #print "Genetics - populate Codons for Crossing on Choice1"
            for self.i in range(len(self.c[self.choice1].g)):
                for self.j in range(len(self.c[self.choice1].g[self.i].c)):
                    for self.l in range(int((self.c[self.choice1].g[self.i].c[self.j].cr)*(self.c[self.choice1].totallen()+self.c[self.choice2].totallen())*100)):
                        self.populace.append(self.i*len(self.c[self.choice1].g[self.i].c)+self.j)
                        self.length1 = self.length1 + 1
            #print "Genetics - populate Codons for Crossing on Choice2"
            for self.i in range(len(self.c[self.choice2].g)):
                for self.j in range(len(self.c[self.choice2].g[self.i].c)):
                    for self.l in range(int((self.c[self.choice2].g[self.i].c[self.j].cr)*(self.c[self.choice1].totallen()+self.c[self.choice2].totallen())*100)):
                        self.populace.append(self.i*len(self.c[self.choice2].g[self.i].c)+self.j)
                        self.length2 = self.length2 + 1
            #print "Genetics - populate the blanks for Crossing"
            for self.i in range(int((self.length1+self.length2)-(self.c[self.choice1].totallen()+self.c[self.choice2].totallen())*100)):
                self.populace.append("")
            self.cross = random.choice(range(len(self.populace)))-1
            if self.populace[self.cross] <> "":
                if self.cross+1 <= self.length1:
                    self.Temp = self.c[self.choice1].split(self.populace[self.cross])
                    self.Temp2 = []
                    if self.populace[self.cross] <= self.c[self.choice2].totallen():
                        self.Temp2 = self.c[self.choice2].split(self.populace[self.cross])
                    if len(self.Temp2.c) > 0 : self.c[self.choice1].append(self.Temp2)
                    self.c[self.choice2].append(self.Temp)
                    self.l = 0
                    for self.i in self.c[self.choice1].g:
                        for self.j in self.i.c:
                            self.j.cr += 0.01 if self.l < self.populace[self.cross] else self.j.cr == 0.3/float(self.c[self.choice1].totallen())
                            self.l += 1
                elif self.cross+1 > self.length1:
                    self.Temp = self.c[self.choice2].split(self.populace[self.cross])
                    self.Temp2 = []
                    if self.populace[self.cross] <= self.c[self.choice1].totallen():
                        self.Temp2 = self.c[self.choice1].split(self.populace[self.cross])
                    if len(self.Temp2.c) > 0 : self.c[self.choice2].append(self.Temp2)
                    self.c[self.choice1].append(self.Temp)
                    self.l = 0
                    for self.i in self.c[self.choice2].g:
                        for self.j in self.i.c:
                            self.j.cr += 0.01 if self.l < self.populace[self.cross] else self.j.cr == 0.3/float(self.c[self.choice2].totallen())
                            self.l += 1
            #print "Genetics - populate for Mutation Rate Choice1"
            for self.i in range(len(self.c[self.choice1].g)):
                for self.j in range(len(self.c[self.choice1].g[self.i].c)):
                    self.Temp = [self.l for self.l in self.rangeset if self.l != self.c[self.choice1].g[self.i].c[self.j].v]
                    self.populace = []
                    for self.l in range(int(self.c[self.choice1].g[self.i].c[self.j].mr*1000)):
                        self.populace.append(random.choice(self.Temp))
                    for self.l in range(int(1000-self.c[self.choice1].g[self.i].c[self.j].mr)):
                        self.populace.append("")
                    self.Choicemr = random.choice(self.populace)
                    if self.Choicemr != "":
                        self.c[self.choice1].g[self.i].c[self.j].v = self.Choicemr
                        self.c[self.choice1].g[self.i].c[self.j].mr = 0.001
                    else:
                        self.c[self.choice1].g[self.i].c[self.j].mr += 0.001
            #print "Genetics - populate for Mutation Rate Choice2"
            for self.i in range(len(self.c[self.choice2].g)):
                for self.j in range(len(self.c[self.choice2].g[self.i].c)):
                    self.Temp = [self.l for self.l in self.rangeset if self.l != self.c[self.choice2].g[self.i].c[self.j].v]
                    self.populace = []
                    for self.l in range(int(self.c[self.choice2].g[self.i].c[self.j].mr*1000)):
                        self.populace.append(random.choice(self.Temp))
                    for self.l in range(int(1000-self.c[self.choice2].g[self.i].c[self.j].mr)):
                        self.populace.append("")
                    self.Choicemr = random.choice(self.populace)
                    if self.Choicemr != "":
                        self.c[self.choice2].g[self.i].c[self.j].v = self.Choicemr
                        self.c[self.choice2].g[self.i].c[self.j].mr = 0.001
                    else:
                        self.c[self.choice2].g[self.i].c[self.j].mr += 0.001
            self.c[self.choice1].reEvalCR()
            self.c[self.choice2].reEvalCR()
            self.Decode(self.choice1)
            self.Decode(self.choice2)
            q_Population.put(self)
        

app = wx.App()
f_GAConfig = f_Config(None)
f_GAConfig.Show()
app.MainLoop()
