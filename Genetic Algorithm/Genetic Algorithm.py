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
import time

t_EVT_REFRESH = wx.NewEventType()
EVT_REFRESH = wx.PyEventBinder(t_EVT_REFRESH, 1)

q_Population = Queue.Queue(1)

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
        self._GPDone = False
        self._ADone = False
        self.pop = self.pop = q_Population.get()

    def runagain(self, parent,selPop=wx.NOT_FOUND,selChrome=wx.NOT_FOUND,selGene=wx.NOT_FOUND):
        self._parent = parent
        self._selPop = selPop
        self._selChrome = selChrome
        self._selGene = selGene
        self._GPDone = False
        self._ADone = False
        self.run()

    def OnRefresh(self, parent, val):
        self._parent = parent
        #print "onrefresh"
        #wx.MessageBox("On Refresh - " + str(val), 'Info',  wx.OK | wx.ICON_INFORMATION)
        

    def run(self):
        while True:
            #print "refresh"
            #if q_Genetics.empty() == False:
            #    populace = q_Genetics.get()
            #    self.pop.p = populace[0][0]
            #    self.pop.c[populace[1][0]] == populace[1][1]
            #    self.pop.c[populace[2][0]] == populace[2][1]
            #if q_Answers.empty() == False:
            #    self.pop.a.append(q_Answers.get())
            #_value = [[self.pop.p,len(self.pop.a)]]
            if not q_Population.empty() : self.pop = q_Population.get()
            if str(self.pop.p) != self._parent.lct_VM_Population.GetItem(0,1).GetText() : self._parent.lct_VM_Population.SetStringItem(0,1,str(self.pop.p))
            if str(len(self.pop.a)) != self._parent.lct_VM_Population.GetItem(1,1).GetText() : self._parent.lct_VM_Population.SetStringItem(1,1,str(len(self.pop.a)))
            if self._selPop == 0:
                #print "selPop = 0"
                self._ADone = False
                #_value.append([])
                #try:
                #    self._parent.lct_VM_Chromosomes.InsertStringItem(i,str(populace[1][0]))
                #    self._parent.lct_VM_Chromosomes.SetStringItem(i,1,str(populace[1][1].Decode(self.pop.iset,self.pop.k)[0]))
                #    self._parent.lct_VM_Chromosomes.SetStringItem(i,2,str(populace[1][1].Decode(self.pop.iset,self.pop.k)[1]))
                #    self._parent.lct_VM_Chromosomes.SetStringItem(i,3,''.join([str(populace[1][1].g[j].c[k].v) for j in range(len(populace[1][1].g)) for k in range(len(populace[1][1].g[j].c))]),)
                #    self._parent.lct_VM_Chromosomes.SetStringItem(i,4,str(populace[1][1].f))
                #    self._parent.lct_VM_Chromosomes.SetStringItem(i,5,str(populace[1][1].cr))
                #    self._parent.lct_VM_Chromosomes.SetStringItem(i,6,str(populace[1][1].GeneLength))
                    #_value[1].append([str(populace[1][0]),
                    #                    str(populace[1][1].Decode(self.pop.iset,self.pop.k)[0]),
                    #                    populace[1][1].Decode(self.pop.iset,self.pop.k)[1],
                    #                    ''.join([str(populace[1][1].g[j].c[k].v) for j in range(len(populace[1][1].g)) for k in range(len(populace[1][1].g[j].c))]),
                    #                    str(populace[1][1].f),
                    #                    str(populace[1][1].cr),
                    #                    str(populace[1][1].GeneLength)])
                #    self._parent.lct_VM_Chromosomes.InsertStringItem(i,str(populace[2][0]))
                #    self._parent.lct_VM_Chromosomes.SetStringItem(i,1,str(populace[2][1].Decode(self.pop.iset,self.pop.k)[0]))
                #    self._parent.lct_VM_Chromosomes.SetStringItem(i,2,str(populace[2][1].Decode(self.pop.iset,self.pop.k)[1]))
                #    self._parent.lct_VM_Chromosomes.SetStringItem(i,3,''.join([str(populace[2][1].g[j].c[k].v) for j in range(len(populace[2][1].g)) for k in range(len(populace[2][1].g[j].c))]),)
                #    self._parent.lct_VM_Chromosomes.SetStringItem(i,4,str(populace[2][1].f))
                #    self._parent.lct_VM_Chromosomes.SetStringItem(i,5,str(populace[2][1].cr))
                #    self._parent.lct_VM_Chromosomes.SetStringItem(i,6,str(populace[2][1].GeneLength))
                    #_value[1].append([str(populace[2][0]),
                    #                    str(populace[2][1].Decode(self.pop.iset,self.pop.k)[0]),
                    #                    populace[2][1].Decode(self.pop.iset,self.pop.k)[1],
                    #                    ''.join([str(populace[2][1].g[j].c[k].v) for j in range(len(populace[2][1].g)) for k in range(len(populace[2][1].g[j].c))]),
                    #                    str(populace[2][1].f),
                    #                    str(populace[2][1].cr),
                    #                    str(populace[2][1].GeneLength)])
                #except:
                #    pass
                if self._GPDone == False:
                    i = 0
                    while i < len(self.pop.c):
                    #for i in range(len(self.pop.c)):
                        print "i " + str(i)
                        if i > self._parent.lct_VM_Chromosomes.GetItemCount()-1:
                            self._parent.lct_VM_Chromosomes.InsertStringItem(i,str(self.pop.c[i].Index))
                        else:
                            print "i " + str(i)
                            print "len " + str(len(self.pop.c))
                            print "index " + str(self.pop.c[i].Index)
                            print "get text " + str(self._parent.lct_VM_Chromosomes.GetItem(i,0).GetText())
                            if str(self.pop.c[i].Index) != self._parent.lct_VM_Chromosomes.GetItem(i,0).GetText() : self._parent.lct_VM_Chromosomes.SetStringItem(i,0,str(self.pop.c[i].Index))
                        #print len(self.pop.c)
                        #print self.pop.c[i].outputData(self.pop.iset,self.pop.k)
                        #print str(self.pop.c[i].Decode(self.pop.iset,self.pop.k)[0])
                        if str(self.pop.c[i].value) != self._parent.lct_VM_Chromosomes.GetItem(i,1).GetText() : self._parent.lct_VM_Chromosomes.SetStringItem(i,1,str(self.pop.c[i].value))
                        if self.pop.c[i].equation != self._parent.lct_VM_Chromosomes.GetItem(i,2).GetText() : self._parent.lct_VM_Chromosomes.SetStringItem(i,2,self.pop.c[i].equation)
                        if self.pop.c[i].codonString != self._parent.lct_VM_Chromosomes.GetItem(i,3).GetText() : self._parent.lct_VM_Chromosomes.SetStringItem(i,3,self.pop.c[i].codonString)
                        if str(self.pop.c[i].f) != self._parent.lct_VM_Chromosomes.GetItem(i,4).GetText() : self._parent.lct_VM_Chromosomes.SetStringItem(i,4,str(self.pop.c[i].f))
                        if str(self.pop.c[i].cr) != self._parent.lct_VM_Chromosomes.GetItem(i,5).GetText() : self._parent.lct_VM_Chromosomes.SetStringItem(i,5,str(self.pop.c[i].cr))
                        if str(len(self.pop.c[i].g)) != self._parent.lct_VM_Chromosomes.GetItem(i,6).GetText() : self._parent.lct_VM_Chromosomes.SetStringItem(i,6,str(len(self.pop.c[i].g)))
                        #_value[1].append([str(i),
                        #                str(self.pop.c[i].Decode(self.pop.iset,self.pop.k)[0]),
                        #                self.pop.c[i].Decode(self.pop.iset,self.pop.k)[1],
                        #                ''.join([str(self.pop.c[i].g[j].c[k].v) for j in range(len(self.pop.c[i].g)) for k in range(len(self.pop.c[i].g[j].c))]),
                        #                str(self.pop.c[i].f),
                        #                str(self.pop.c[i].cr),
                        #                str(self.pop.c[i].GeneLength)])
                        i += 1
                    for i in range(len(self.pop.c),self._parent.lct_VM_Chromosomes.GetItemCount()):
                        self._parent.lct_VM_Chromosomes.DeleteItem(len(self.pop.c))
                        if self._selChrome >= len(self.pop.c) : self._selChrome = len(self.pop.c)-1
                    self._GPDone == True
                if self._selChrome != wx.NOT_FOUND:
                    for j in range(len(self.pop.c[self._selChrome].g)):
                        #print "j " + str(j)
                        if j > self._parent.lct_VM_Genes.GetItemCount()-1:
                            self._parent.lct_VM_Genes.InsertStringItem(j,str(j))
                        else:
                            if str(j) != self._parent.lct_VM_Genes.GetItem(j,0).GetText() : self._parent.lct_VM_Genes.SetStringItem(j,0,str(j))
                        if self.pop.c[self._selChrome].g[j].value != self._parent.lct_VM_Genes.GetItem(j,1).GetText() : self._parent.lct_VM_Genes.SetStringItem(j,1,self.pop.c[self._selChrome].g[j].value)
                        if self.pop.c[self._selChrome].g[j].codonString != self._parent.lct_VM_Genes.GetItem(j,2).GetText() : self._parent.lct_VM_Genes.SetStringItem(j,2,self.pop.c[self._selChrome].g[j].codonString)
                        if str(len(self.pop.c[self._selChrome].g[j].c)) != self._parent.lct_VM_Genes.GetItem(j,3).GetText() : self._parent.lct_VM_Genes.SetStringItem(j,3,str(len(self.pop.c[self._selChrome].g[j].c)))
                        #_value[2].append([str(j),
                        #                    self.pop.c[i].g[j].Decode(self.pop.k,self.pop.rangeset),
                        #                    ''.join([self.pop.c[i].g[j].c[k].v for k in range(len(self.pop.c[i].g[j].c))]),
                        #                    str(len(self.pop.c[i].g[j].c))])
                    if self._selGene != wx.NOT_FOUND:
                        for k in range(len(self.pop.c[self._selChrome].g[self._selGene].c)):
                            if k > self._parent.lct_VM_Codons.GetItemCount()-1:
                                self._parent.lct_VM_Codons.InsertStringItem(k,str(k))
                            else:
                                self._parent.lct_VM_Codons.SetStringItem(k,0,str(k))
                            self._parent.lct_VM_Codons.SetStringItem(k,1,str(self.pop.c[self._selChrome].g[self._selGene].c[k].v))
                            self._parent.lct_VM_Codons.SetStringItem(k,2,str(self.pop.c[self._selChrome].g[self._selGene].c[k].cr))
                            self._parent.lct_VM_Codons.SetStringItem(k,3,str(self.pop.c[self._selChrome].g[self._selGene].c[k].mr))
                            #_value.append([str(k),
                            #                str(self.pop.c[i].g[j].c[k].v),
                            #                str(self.pop.c[i].g[j].c[k].cr),
                            #                str(self.pop.c[i].g[j].c[k].mr)])
                        for k in range(len(self.pop.c[self._selChrome].g[self._selGene].c), self._parent.lct_VM_Codons.GetItemCount()):
                            self._parent.lct_VM_Codons.DeleteItem(len(self.pop.c[self._selChrome].g[self._selGene].c))
                    for j in range(len(self.pop.c[self._selChrome].g), self._parent.lct_VM_Genes.GetItemCount()):
                        self._parent.lct_VM_Genes.DeleteItem(len(self.pop.c[self._selChrome].g))
                        if self._selGene >= len(self.pop.c[self._selChrome].g) : self._selGene = len(self.pop.c[self._selChrome].g)-1
            elif self._selPop == 1:
                #print "selPop = 1"
                self._GPDone = False
                if self._ADone == False:
                    i = 0
                    while i < len(self.pop.a):
                    #for i in range(len(self.pop.a)):
                        #print "i " + str(i)
                        if i > self._parent.lct_VM_Chromosomes.GetItemCount()-1:
                            self._parent.lct_VM_Chromosomes.InsertStringItem(i,str(i))
                        else:
                            self._parent.lct_VM_Chromosomes.SetStringItem(i,0,str(i))
                        self._parent.lct_VM_Chromosomes.SetStringItem(i,1,str(self.pop.a[i].Decode(self.pop.iset,self.pop.k)[0]))
                        self._parent.lct_VM_Chromosomes.SetStringItem(i,2,self.pop.a[i].Decode(self.pop.iset,self.pop.k)[1])
                        self._parent.lct_VM_Chromosomes.SetStringItem(i,3,''.join([str(self.pop.a[i].g[j].c[k].v) for j in range(len(self.pop.a[i].g)) for k in range(len(self.pop.a[i].g[j].c))]))
                        self._parent.lct_VM_Chromosomes.SetStringItem(i,4,str(self.pop.a[i].f))
                        self._parent.lct_VM_Chromosomes.SetStringItem(i,5,str(self.pop.a[i].cr))
                        self._parent.lct_VM_Chromosomes.SetStringItem(i,6,str(self.pop.a[i].GeneLength))
                        #_value[1].append([str(i),
                        #                str(self.pop.a[i].Decode(self.pop.iset,self.pop.k)[0]),
                        #                self.pop.a[i].Decode(self.pop.iset,self.pop.k)[1],
                        #                ''.join([str(self.pop.a[i].g[j].c[k].v) for j in range(len(self.pop.a[i].g)) for k in range(len(self.pop.a[i].g[j].c))]),
                        #                str(self.pop.a[i].f),
                        #                str(self.pop.a[i].cr),
                        #                str(self.pop.a[i].GeneLength)])
                        i += 1
                    for i in range(len(self.pop.a),self._parent.lct_VM_Chromosomes.GetItemCount()):
                        self._parent.lct_VM_Chromosomes.DeleteItem(len(self.pop.a))
                    self._ADone = True
                if self._selChrome != wx.NOT_FOUND:
                    _value.append([])
                    for j in range(len(self.pop.a[i].g)):
                        #print "j " + str(j)
                        if j > self._parent.lct_VM_Genes.GetItemCount()-1:
                            self._parent.lct_VM_Genes.InsertStringItem(i,str(j))
                        else:
                            self._parent.lct_VM_Genes.SetStringItem(i,str(j))
                        self._parent.lct_VM_Genes.SetStringItem(i,1,self.pop.a[i].g[j].Decode(self.pop.k,self.pop.rangeset))
                        self._parent.lct_VM_Genes.SetStringItem(i,2,''.join([self.pop.a[i].g[j].c[k].v for k in range(len(self.pop.a[i].g[j].c))]))
                        self._parent.lct_VM_Genes.SetStringItem(i,3,str(len(self.pop.a[i].g[j].c)))
                        #_value[2].append([str(j),
                        #                    self.pop.a[i].g[j].Decode(self.pop.k,self.pop.rangeset),
                        #                    ''.join([self.pop.a[i].g[j].c[k].v for k in range(len(self.pop.a[i].g[j].c))]),
                        #                    str(len(self.pop.a[i].g[j].c))])
                    if self._selGene != wx.NOT_FOUND:
                        _value.append([])
                        for k in range(len(self.pop.a[i].g[j].c)):
                            if k > self._parent.lct_VM_Codons.GetItemCount()-1:
                                self._parent.lct_VM_Codons.InsertStringItem(i,str(k))
                            else:
                                self._parent.lct_VM_Codons.SetStringItem(i,str(k))
                            self._parent.lct_VM_Codons.SetStringItem(i,1,str(self.pop.a[i].g[j].c[k].v))
                            self._parent.lct_VM_Codons.SetStringItem(i,2,str(self.pop.a[i].g[j].c[k].cr))
                            self._parent.lct_VM_Codons.SetStringItem(i,3,str(self.pop.a[i].g[j].c[k].mr))
                            #_value.append([str(k),
                            #                str(self.pop.a[i].g[j].c[k].v),
                            #                str(self.pop.a[i].g[j].c[k].cr),
                            #                str(self.pop.a[i].g[j].c[k].mr)])
                        for k in range(len(self.pop.a[self._selChrome].g[self._selGene].c), self._parent.lct_VM_Codons.GetItemCount()):
                            self._parent.lct_VM_Codons.DeleteItem(len(self.pop.a[self._selChrome].g[self._selGene].c))
                    for j in range(len(self.pop.a[self._selChrome].g), self._parent.lct_VM_Genes.GetItemCount()):
                        self._parent.lct_VM_Genes.DeleteItem(len(self.pop.a[self._selChrome].g))
                    else:
                        self._parent.lct_VM_Codons.DeleteAllItems()
                else:
                    self._parent.lct_VM_Genes.DeleteAllItems()
            else:
                self._parent.lct_VM_Chromosomes.DeleteAllItems()
            
            #merge loops
            """val = _value
            for i in range(len(val)):
                print 'First For i = ' + str(i)
                for j in range(len(val[i])):
                    print 'First For i = ' + str(i) + ' j = ' + str(j)
                    if i == 0:
                        print "First 0"
                        self._parent.lct_VM_Population.SetStringItem(j,1,str(val[i][j]))
                    elif i == 1:
                        print "First 1"
                        for k in range(len(val[i][j])):
                            if int(val[i][j][0]) > self._parent.lct_VM_Chromosomes.GetItemCount()-1:
                                self._parent.lct_VM_Chromosomes.InsertStringItem(int(val[i][j][0]),val[i][j][k])
                            else:
                                self._parent.lct_VM_Chromosomes.SetStringItem(int(val[i][j][0]),k,val[i][j][k])
                    elif i == 2:
                        print "First 2"
                        #wx.MessageBox('2', 'Info',  wx.OK | wx.ICON_INFORMATION)
                        for k in range(len(val[i][j])):
                            if int(val[i][j][0]) > self._parent.lct_VM_Genes.GetItemCount()-1:
                                self._parent.lct_VM_Genes.InsertStringItem(j,val[i][j][k])
                            else:
                                self._parent.lct_VM_Genes.SetStringItem(j,k,val[i][j][k])
                    elif i == 3:
                        print "First 3"
                        #wx.MessageBox('3', 'Info',  wx.OK | wx.ICON_INFORMATION)
                        for k in range(len(val[i][j])):
                            if int(val[i][j][0]) > self._parent.lct_VM_Codons.GetItemCount()-1:
                                self._parent.lct_VM_Codons.InsertStringItem(j,val[i][j][k])
                            else:
                                self._parent.lct_VM_Codons.SetStringItem(j,k,val[i][j][k])"""
            #wx.MessageBox('After First For', 'Info',  wx.OK | wx.ICON_INFORMATION)
            #if self._parent.PopSel != wx.NOT_FOUND:
            #    print "Population Selected"
            #    for i in range(1,len(_val)):
            #        if i == 1:
            #            print "Second 1"
            #            for j in range(len(val[i]), self._parent.lct_VM_Chromosomes.GetItemCount()):
            #                self._parent.lct_VM_Chromosomes.DeleteItem(j)
            #        elif i == 2:
            #            print "Second 2"
            #            for j in range(len(val[i]), self._parent.lct_VM_Genes.GetItemCount()):
            #                self._parent.lct_VM_Genes.DeleteItem(j)
            #        elif i == 3:
            #            print "Second 3"
            #            for j in range(len(val[i]), self._parent.lct_VM_Codons.GetItemCount()):
            #                self._parent.lct_VM_Codons.DeleteItem(j)
            #    for i in range(len(val),4):
            #        if i == 2:
            #            print "Third 2"
            #            self._parent.lct_VM_Genes.DeleteAllItems()
            #        elif i == 3:
            #            print "Third 3"
            #            self._parent.lct_VM_Codons.DeleteAllItems()
            #else:
            #    print "No Population Selected"
            #    self._parent.lct_VM_Chromosomes.DeleteAllItems()
            #    self._parent.lct_VM_Genes.DeleteAllItems()
            #    self._parent.lct_VM_Codons.DeleteAllItems()
            #print "After Last For"
            #wx.MessageBox('After Last For', 'Info',  wx.OK | wx.ICON_INFORMATION)
            #self.lct_VM_Population.SetItemState(0,wx.LIST_STATE_SELECTED, wx.LIST_STATE_SELECTED)
            #worker = Refresh(self, self.PopSel,self.ChromeSel, self.GeneSel)
            #print "Created worker"
            self._selPop = self._parent.PopSel
            self._selChrome = self._parent.ChromeSel
            self._selGene = self._parent.GeneSel
            #print "End On Refresh"
                            
        """if self._selPop == 0:
            _value.append([])
            for i in range(len(populace.c)):
                print "i " + str(i)
                _value[1].append([str(i),
                                    str(populace.c[i].Decode(populace.iset,populace.k)[0]),
                                    populace.c[i].Decode(populace.iset,populace.k)[1],
                                    ''.join([str(populace.c[i].g[j].c[k].v) for j in range(len(populace.c[i].g)) for k in range(len(populace.c[i].g[j].c))]),
                                    str(populace.c[i].f),
                                    str(populace.c[i].cr),
                                    str(populace.c[i].GeneLength)])
                if self._selChrome != wx.NOT_FOUND:
                    _value.append([])
                    for j in range(len(populace.c[i].g)):
                        print "j " + str(j)
                        _value[2].append([str(j),
                                            populace.c[i].g[j].Decode(populace.k,populace.rangeset),
                                            ''.join([populace.c[i].g[j].c[k].v for k in range(len(populace.c[i].g[j].c))]),
                                            str(len(populace.c[i].g[j].c))])
                        if self._selGene != wxNOT_FOUND:
                            _value.append([])
                            for k in range(len(populace.c[i].g[j].c)):
                                _value.append([str(k),
                                                    str(populace.c[i].g[j].c[k].v),
                                                    str(populace.c[i].g[j].c[k].cr),
                                                    str(populace.c[i].g[j].c[k].mr)])
                                #evt = RefreshEvent(t_EVT_REFRESH, -1, _value)
                                #print "post refresh"
                                #wx.PostEvent(self._parent,evt)
                        #else:
                            #evt = RefreshEvent(t_EVT_REFRESH, -1, _value)
                            #print "post refresh"
                            #wx.PostEvent(self._parent,evt)
                #else:
                    #evt = RefreshEvent(t_EVT_REFRESH, -1, _value)
                    #print "post refresh"
                    #wx.PostEvent(self._parent,evt)
        elif self._selPop == 1:
            _value.append([])
            for i in range(len(populace.a)):
                _value[1].append([str(i),
                                    str(populace.c[i].Decode(populace.iset,populace.k)[0]),
                                    populace.a[i].Decode(populace.iset,populace.k)[1],
                                    ''.join([populace.a[i].g[j].c[k].v for k in range(len(populace.a[i].g[j].c)) for j in range(len(populace.c[i].g))]),
                                    str(populace.a[i].f),
                                    str(populace.a[i].cr),
                                    str(populace.a[i].GeneLength)])
                if self._selChrome != wx.NOT_FOUND:
                    _value.append([])
                    for j in range(len(populace.a[i].g)):
                        _value[2].append([[str(j),
                                            populace.a[i].g[j].Decode(populace.k,populace.rangeset),
                                            ''.join([populace.a[i].g[j].c[k].v for k in range(len(populace.a[i].g[j].c))]),
                                            str(len(populace.a[i].g[j].c))]])
                        if self._selGene != wxNOT_FOUND:
                            _value.append([])
                            for k in range(len(populace.a[i].g[j].c)):
                                _value[3].append([])
                                _value.append([str(k),
                                                    str(populace.a[i].g[j].c[k].v),
                                                    str(populace.a[i].g[j].c[k].cr),
                                                    str(populace.a[i].g[j].c[k].mr)])
                                #evt = RefreshEvent(t_EVT_REFRESH, -1, _value)
                                #print "post refresh"
                                #wx.PostEvent(self._parent,evt)
                        #else:
                            #evt = RefreshEvent(t_EVT_REFRESH, -1, _value)
                            #print "post refresh"
                            #wx.PostEvent(self._parent,evt)
                #else:
                    #evt = RefreshEvent(t_EVT_REFRESH, -1, _value)
                    #print "post refresh"
                    #wx.PostEvent(self._parent,evt)
        #else:"""
        #print "post refresh"
        self.OnRefresh(self._parent,_value)


###########################################################################
## Class f_Viewer
###########################################################################

class f_Viewer ( wx.Frame ):
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Genetic Algorithm Viewer - ", pos = wx.DefaultPosition, size = wx.Size( 500,835 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
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

        self.t_pop = threading.Thread(target=Populate,args=(self.Population,self.InstructionSet,self.KeySet,self.CLengthSet,self.RangeSet,self.GLength,self.Answer))
        self.t_pop.start()
        #wx.MessageBox('2', 'Info',  wx.OK | wx.ICON_INFORMATION)
        self.worker = Refresh(self, self.PopSel,self.ChromeSel, self.GeneSel)
        self.worker.start()

        self.Show()

    def OnPopSel(self, evt):
        self.PopSel = evt.GetIndex()
        #print self.PopSel

    def OnChromeSel(self, evt):
        self.ChromeSel = evt.GetIndex()

    def OnGeneSel(self, evt):
        self.GeneSel = evt.GetIndex()
        
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
        
        lbx_CMI_LibraryChoices = ["isint(gval)","isoperator(gval)"]
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
        self.value = ""
        for i in range(length):
            self.c.append(Codon(random.choice(rangeset), crossrate))
        self.codonString = ''.join([str(i.v) for i in self.c])

    def Decode(self, key, rangeset):
        index = 0
        for i in range(len(self.c)):
            index = index + self.c[i].v*len(rangeset)**(len(self.c)-i-1)
        if index >= len(key):
            return ""
        else:
            return key[index]

class Chromosome():
    def __init__(self, parent, Index, length, rangeset, glength, fitness):
        self.r = rangeset
        self.cr = 0.3
        self.f = fitness
        self.GeneLength = glength
        self.g = []
        self.value = 0
        self.Index = Index
        self.parent = parent
        self.equation = ""
        
        for i in range(length):
            self.g.append(Gene(self.r, glength, self.cr/(float(length)*float(glength))))
        self.codonString = ''.join([str(j.v) for i in self.g for j in i.c])
        

    def Decode(self, instructionset, key):
        val = []
        j = 0
        for i in range(len(self.g)):
            gval = self.g[i].Decode(key,self.r)
            self.g[i].value = gval
            check = eval(instructionset[j%len(instructionset)])
            if check:
                val.append(gval)
                j = j+1
        if len(val) != 0:
            val = ''.join(val)
            if val != "":
                try:
                    return [eval(val),val]
                except:
                    return ["",""]
            else:
                return [val,val]
        else:
            return ["",""]

    def totallen(self):
        val = 0
        for i in range(len(self.g)):
            val = val + len(self.g[i].c)
        return val

    def split(self, Index):
        newGene = Gene([0,1],self.totallen()-Index,0.1)
        k = 0
        l = 0
        m = 0
        for i in range(len(self.g)):
            m = 0
            for j in range(len(self.g[i].c)):
                m = j
                if k == Index : break
                k = k + 1
            l = i
            if k == Index : break
        #c_orglen =
        #print self.outputData(self.parent.iset,self.parent.k)
        for i in range(Index, self.totallen()):
            #print self.g[int(math.floor(i/len(self.g)))].c[Index%len(self.g[int(math.floor(Index/len(self.g)))].c)]
            #if Index%len(self.g[int(math.floor(Index/g_orglen))].c) == 0 : c_orglen = len(self.g[int(math.floor(Index/g_orglen))].c)
            newGene.c[i-Index] = self.g[l].c.pop(m)
            for j in range(l+1,len(self.g)):
                if len(self.g[j].c) == 0:
                    #print "test"
                    self.g.pop(j)
                else:
                    self.g[j-1].c.append(self.g[j].c.pop(0))
            try:
                if len(self.g[j].c) == 0:
                    self.g.pop(j)
            except:
                pass
        #for i in range(len(self.g)):
            #print self.outputData(self.parent.iset,self.parent.k)
            #print i
            #print len(self.g)
            #print Index
            #print Index/len(self.g)"""
            #if i >= Index/len(self.g):
                #self.g.pop(i)
        #print ''.join([str(newGene.c[i].v) for i in range(len(newGene.c))])
        #print "Split - " + str(len(self.g))
        return newGene

    def append(self, newGene):
        #print ''.join([str(newGene.c[i].v) for i in range(len(newGene.c))])
        bnone = True
        #print "test 1"
        for i in range(len(self.g)):
            if self.g[i].glength > len(self.g[i].c):
                bnone = False
                break
        if bnone == False:
            for j in range(len(self.g[i].c),self.g[i].glength):
                #print j
                if len(newGene.c) > 0 : self.g[i].c.append(newGene.c.pop(0))
        #print "test 2"
        while len(newGene.c) > 0:
            Temp = Gene([0,1], self.GeneLength, 0.1)
            #print "Append - 1 - NewGene Length" + str(len(newGene.c))
            #print "Append - 2 - NewGene Codons - " + ''.join([str(newGene.c[i].v) for i in range(len(newGene.c))])
            #print len(Temp.c)
            if len(newGene.c) > len(Temp.c):
                #print "test 3"
                for i in range(len(Temp.c)):
                    Temp.c[i] = newGene.c.pop(0)
                self.g.append(Temp)
            else:
                #print "Append 3 - NewGene Length - " + str(len(newGene.c))
                #print ''.join([str(newGene.c[i].v) for i in range(len(newGene.c))])
                #wx.MessageBox("Append 1 - ", 'Info',  wx.OK | wx.ICON_INFORMATION)
                self.g.append(newGene)
                #print "Append - After Append"
                #print self.outputData(self.parent.iset,self.parent.k)
                break
            #print "Append - 4 - Temp Codons - " + ''.join([str(i.v) for i in Temp.c])
            
        #print "Split - " + str(len(self.g))

    def reEvalCR(self):
        self.cr = 0
        for i in self.g:
            for j in i.c:
                self.cr += j.cr
            i.codonString = ''.join([str(j.v) for j in i.c])
        self.codonString = ''.join([str(j.v) for i in self.g for j in i.c])

    def outputData(self, InstSet, Key):
        Temp = self.Decode(InstSet, Key)
        return '\n'.join([str(self.Index),
                         "Total Length - " + str(self.totallen()),
                         "Fitness Value" + str(self.f),
                         "Decoded Information - " + str(Temp),
                         "Binary Data - " + ''.join([str(j.v) for i in self.g for j in i.c]),
                         "Length of the Genes - " + str(self.GeneLength),
                         "Amount of Genes - " + str(len(self.g)),
                         "Codon Data",
                         "Value, Cross Rate, Mutation Rate",
                         '\n'.join([','.join([str(k) for k in [j.v,j.cr,j.mr]]) for i in self.g for j in i.c])])

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
            self.c.append(Chromosome(self,i,random.choice(lengthrange),rangeset,glength,1))
        oldpop = self.p
        for i in range(self.p):
            self.Decode(i-(oldpop-self.p))
        q_Population.put(self)
        self.Genetics()
            
    def Decode(self, ichromosome):
        value = self.c[ichromosome].Decode(self.iset, self.k)
        equation = value[1]
        value = value[0]
        if value != "":
            self.c[ichromosome].value = value
            self.c[ichromosome].equation = equation
            if value == self.Answer:
                self.a.append(self.c.pop(ichromosome))
                self.p = self.p - 1
                #print equation
                #if self.p%50 == 0 : print "Chromosomes Remaining - " + str(self.p)
            else:
                self.c[ichromosome].f = self.Answer-abs(self.Answer-value)
                if self.c[ichromosome].f < 1 : self.c[ichromosome].f = 1
                
            return value
        else:
            self.c.pop(ichromosome)
            self.p = self.p - 1
            #if self.p%50 == 0 : print "Chromosomes Remaining - " + str(self.p)

    def Genetics(self):
        while self.p > 1:
            populace = []
            #print "Genetics - populate for Choice1"
            #print str(self.p)
            #for i in range(self.p):
            #    for j in range(int(self.p*self.c[i].f)):
            #        populace.append(i)
            #choice1 = random.choice(populace)
            choice1 = weighted_choice([[i,self.c[i].f] for i in range(self.p)])
            #print choice1
            #print self.c[choice1].f
            #self.c[choice1].f = 1/float(self.p)
            self.c[choice1].f = 1
            #wx.MessageBox("Genetics 1 - " + self.c[choice1].outputData(self.iset, self.k), 'Info',  wx.OK | wx.ICON_INFORMATION)
            populace = []
            #print "Genetics - populate for Choice2"
            #for i in range(self.p):
            #    if i != choice1:
            #        for j in range(int(self.p*self.c[i].f)):
            #            populace.append(i)
            #print len(populace)
            #choice2 = random.choice(populace)
            choice2 = weighted_choice([[i,self.c[i].f] for i in range(self.p) if i != choice1])
            #self.c[choice2].f = 1/float(self.p)
            self.c[choice2].f = 1
            #wx.MessageBox("Genetics 2 - " + self.c[choice2].outputData(self.iset, self.k), 'Info',  wx.OK | wx.ICON_INFORMATION)
            populace = []
            length1 = 0
            length2 = 0
            #print "Genetics - populate Codons for Crossing on Choice1"
            for i in range(len(self.c[choice1].g)):
                for j in range(len(self.c[choice1].g[i].c)):
                    for l in range(int((self.c[choice1].g[i].c[j].cr)*(self.c[choice1].totallen()+self.c[choice2].totallen())*100)):
                        populace.append(i*len(self.c[choice1].g[i].c)+j)
                        length1 = length1 + 1
            #print "Genetics - populate Codons for Crossing on Choice2"
            for i in range(len(self.c[choice2].g)):
                for j in range(len(self.c[choice2].g[i].c)):
                    for l in range(int((self.c[choice2].g[i].c[j].cr)*(self.c[choice1].totallen()+self.c[choice2].totallen())*100)):
                        populace.append(i*len(self.c[choice2].g[i].c)+j)
                        length2 = length2 + 1
            #print "Genetics - populate the blanks for Crossing"
            for i in range(int((length1+length2)-(self.c[choice1].totallen()+self.c[choice2].totallen())*100)):
                populace.append("")
            cross = random.choice(range(len(populace)))-1
            #print self.c[choice1].outputData(self.iset,self.k)
            #print self.c[choice2].outputData(self.iset,self.k)
            #wx.MessageBox("Genetics 3 - ", 'Info',  wx.OK | wx.ICON_INFORMATION)
            if populace[cross] <> "":
                if cross+1 <= length1:
                    #print "cross " + str(populace[cross])
                    Temp = self.c[choice1].split(populace[cross])
                    Temp2 = 0
                    if populace[cross] <= self.c[choice2].totallen():
                        Temp2 = self.c[choice2].split(populace[cross])
                        #print "test"
                    #print Temp2
                    if Temp2 != 0 : self.c[choice1].append(Temp2)
                    self.c[choice2].append(Temp)
                    #print "Genetic - After append"
                    #print self.c[choice2].outputData(self.iset,self.k)
                    l = 0
                    for i in self.c[choice1].g:
                        for j in i.c:
                            j.cr += 0.01 if l < populace[cross] else j.cr == 0.3/float(self.c[choice1].totallen())
                            l += 1
                elif cross+1 > length1:
                    #print "cross " + str(populace[cross])
                    Temp = self.c[choice2].split(populace[cross])
                    Temp2 = 0
                    if populace[cross] <= self.c[choice1].totallen():
                        Temp2 = self.c[choice1].split(populace[cross])
                        #print "test"
                    #print Temp2
                    if Temp2 != 0 : self.c[choice2].append(Temp2)
                    self.c[choice1].append(Temp)
                    #print "Genetic - After append"
                    #print self.c[choice1].outputData(self.iset,self.k)
                    l = 0
                    for i in self.c[choice2].g:
                        for j in i.c:
                            j.cr += 0.01 if l < populace[cross] else j.cr == 0.3/float(self.c[choice2].totallen())
                            l += 1
            #wx.MessageBox("Genetics 4 - " + self.c[choice1].outputData(self.iset, self.k), 'Info',  wx.OK | wx.ICON_INFORMATION)
            #wx.MessageBox("Genetics 5 - " + self.c[choice2].outputData(self.iset, self.k), 'Info',  wx.OK | wx.ICON_INFORMATION)
            for i in self.c[choice1].g:
                if len(i.c) == 0:
                    wx.MessageBox("Genetics 4 - " + self.c[choice1].outputData(self.iset, self.k), 'Info',  wx.OK | wx.ICON_INFORMATION)
            for i in self.c[choice2].g:
                if len(i.c) == 0:
                    wx.MessageBox("Genetics 4 - " + self.c[choice2].outputData(self.iset, self.k), 'Info',  wx.OK | wx.ICON_INFORMATION)
            #print "Genetics - populate for Mutation Rate Choice1"
            for i in range(len(self.c[choice1].g)):
                for j in range(len(self.c[choice1].g[i].c)):
                    Temp = [l for l in self.rangeset if l != self.c[choice1].g[i].c[j].v]
                    populace = []
                    for l in range(int(self.c[choice1].g[i].c[j].mr*1000)):
                        populace.append(random.choice(Temp))
                    for l in range(int(1000-self.c[choice1].g[i].c[j].mr*1000)):
                        populace.append("")
                    Choicemr = random.choice(populace)
                    if Choicemr != "":
                        self.c[choice1].g[i].c[j].v = Choicemr
                        self.c[choice1].g[i].c[j].mr = 0.001
                    else:
                        self.c[choice1].g[i].c[j].mr += 0.001
            #wx.MessageBox("Genetics 6 - " + self.c[choice1].outputData(self.iset, self.k), 'Info',  wx.OK | wx.ICON_INFORMATION)
            #print "Genetics - populate for Mutation Rate Choice2"
            for i in range(len(self.c[choice2].g)):
                for j in range(len(self.c[choice2].g[i].c)):
                    Temp = [l for l in self.rangeset if l != self.c[choice2].g[i].c[j].v]
                    populace = []
                    for l in range(int(self.c[choice2].g[i].c[j].mr*1000)):
                        populace.append(random.choice(Temp))
                    for l in range(int(1000-self.c[choice2].g[i].c[j].mr*1000)):
                        populace.append("")
                    Choicemr = random.choice(populace)
                    if Choicemr != "":
                        self.c[choice2].g[i].c[j].v = Choicemr
                        self.c[choice2].g[i].c[j].mr = 0.001
                    else:
                        self.c[choice2].g[i].c[j].mr += 0.001
            #wx.MessageBox("Genetics 7 - " + self.c[choice2].outputData(self.iset, self.k), 'Info',  wx.OK | wx.ICON_INFORMATION)
            self.c[choice1].reEvalCR()
            self.c[choice2].reEvalCR()
            prepop = self.p
            self.Decode(choice1)
            self.Decode(choice2-(prepop-self.p))
            #print str(self.p)
            if q_Population.empty() == True : q_Population.put(self)#q_Genetics.put([[self.p,self.a],[choice1,self.c[choice1]],[choice2,self.c[choice2]]])

def weighted_choice(choices):
   total = sum(w for c, w in choices)
   r = random.uniform(0, total)
   upto = 0
   for c, w in choices:
      if upto + w >= r:
         return c
      upto += w
   assert False, "Shouldn't get here"

        

app = wx.App()
f_GAConfig = f_Config(None)
f_GAConfig.Show()
app.MainLoop()
