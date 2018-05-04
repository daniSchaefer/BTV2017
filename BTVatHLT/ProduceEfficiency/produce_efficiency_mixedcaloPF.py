import sys
import math
import ROOT
import matplotlib.pyplot as plt

from ROOT import TH1F, TH2F, TEfficiency
from matplotlib.pyplot import figure, show
from numpy import arange, sin, pi



def SelectTrigger(event,triggerpath,base=False,btagsequence="Calo",njet=-1):
    # Performances of the PF online b-tagging sequence based on events triggered by HLT_PFHT300PT30_QuadPFJet_75_60_45_40, and studying the CSV cut of the HLT_PFHT300PT30_QuadPFJet_75_60_45_40_TriplePFBTagCSV_3p0
    if triggerpath.find("HLT_PFHT300PT30_QuadPFJet_75_60_45_40")!=-1:
        if base:
            if event.HLT_PFHT300PT30_QuadPFJet_75_60_45_40 : return True
            else: return False
        if not base and njet==-1:
            print "if not base trigger, the number of the jet under current consideratio has to be given!"
            return 0
        if not base:
            if btagsequence.find("Calo")!=-1:
                if event.caloJet_hltBTagCaloCSVp05Double[njet]: return True
                else: return False
            else:
                if event.pfJet_hltBTagPFCSVp070Triple[njet]:return True
                else:return False
    # Performances studes for the b-tagging sequence based on events triggered by 
    #HLT_PFHT430_SixJet40
    #HLT_PFHT430_SixJet40_BTagCSV_p080_v1
    #this is a trigger that only uses PF jets to run the b-tagging sequence on!
    if triggerpath.find("HLT_PFHT430_SixJet40")!=-1:
        if base:
            if event.HLT_PFHT430_SixPFJet40 : return True
            else: return False
        if not base and njet==-1:
            print "if not base trigger, the number of the jet under current consideratio has to be given!"
            return 0
        if not base:
            if btagsequence.find("Calo")!=-1:
                return False
            else:
                if event.pfJet_hltBTagPFCSVp080Single[njet]:return True
                else:return False
    else:
        print "trigger path not found!"
        return 0
                
            



def main() :
    triggerpath="HLT_PFHT300PT30_QuadPFJet_75_60_45_40"
    triggerpath="HLT_PFHT430_SixJet40"
    # Files
    f_ntuple            = ROOT.TFile(sys.argv[1], "READ")
    f_results           = ROOT.TFile(sys.argv[2], "RECREATE")
    f_results.cd()

    # Functions
    makePlots(f_ntuple,  f_results,triggerpath)

def makePlots(f_ntuple, f_results, triggerpath) :

    t = f_ntuple.Get("tree")
    print "Tree extracted..."

    h_csv_inc_4Calo     = TH1F("h_csv_inc_4Calo",    		"h_csv_inc_4Calo",     	50,  0,  1)
    h_csv_inc_4PF      	= TH1F("h_csv_inc_4PF",    		"h_csv_inc_4PF",     	50,  0,  1)
    h_csv_afcalo       	= TH1F("h_csv_afcalo",  	"h_csv_afcalo",      	50,  0,  1)
    h_csv_afpf		= TH1F("h_csv_afpf",		"h_csv_afpf",		50,  0,  1)

    h_csv_inc_log_4Calo     = TH1F("h_csv_inc_log_4Calo",    		"h_csv_inc_log_4Calo",     	50,  0,  7)
    h_csv_inc_log_4PF       = TH1F("h_csv_inc_log_4PF",    		"h_csv_inc_log_4PF",     	50,  0,  7)
    h_csv_afcalo_log	= TH1F("h_csv_afcalo_log",  	"h_csv_afcalo_log",	50,  0,  7)
    h_csv_afpf_log	= TH1F("h_csv_afpf_log",	"h_csv_afpf_log",	50,  0,  7)

    h_csv_inc_calo      = TH1F("h_csv_inc_calo",   	"h_csv_inc_calo",     	50,  0,  1)
    h_csv_inc_pf       	= TH1F("h_csv_inc_pf",  	"h_csv_inc_pf",      	50,  0,  1)
    h_csv_calo_pf	= TH1F("h_csv_calo_pf",		"h_csv_calo_pf",	50,  0,  1)

    h_csv_inc_calo_log	= TH1F("h_csv_inc_calo_log",    "h_csv_inc_calo_log",   50,  0,  7)
    h_csv_inc_pf_log	= TH1F("h_csv_inc_pf_log",  	"h_csv_inc_pf_log",     50,  0,  7)
    h_csv_calo_pf_log	= TH1F("h_csv_calo_pf_log",	"h_csv_calog_pf_log",	50,  0,  7)


    eff_csv_inc_calo    = TEfficiency("eff_csv_inc_calo", "eff_csv_inc_calo",     	50,  0,  1)
    eff_csv_inc_pf      = TEfficiency("eff_csv_inc_pf",    "eff_csv_inc_pf",      	50,  0,  1)
    eff_csv_calo_pf	= TEfficiency("eff_csv_calo_pf",   "eff_csv_calo_pf",          50,  0,  1)

    eff_csv_inc_calo_log  = TEfficiency("eff_csv_inc_calo_log",  "eff_csv_inc_calo_log",   50,  0,  7)
    eff_csv_inc_pf_log	  = TEfficiency("eff_csv_inc_pf_log",    "eff_csv_inc_pf_log",     50,  0,  7)
    eff_csv_calo_pf_log	  = TEfficiency("eff_csv_calo_pf_log",	  "eff_csv_calog_pf_log",   50,  0,  7)


    i = 0

    for event in t:
        print
	print "New event --------"
	print
        
        if not SelectTrigger(event,triggerpath,True) : continue

	print "CALO JET SECTION : # calo jet = ", event.caloJet_num
	for i in range(0, event.caloJet_num-1) :	
		if event.caloJet_offmatch[i] >= 0 :
			print "calo jet[", i, "]"
			print "event.caloJet_offmatch[i]: ", 	event.caloJet_offmatch[i], 	" event.offJet_num: ", 	event.offJet_num
			print "calo pt: ", 			event.caloJet_pt[i], 		" offline pt: ",	event.offJet_pt[  event.caloJet_offmatch[i] ]
			print "calo eta: ",			event.caloJet_eta[i],		" offline eta: ",	event.offJet_eta[ event.caloJet_offmatch[i] ]
			print "calo phi: ",			event.caloJet_phi[i],		" offline phi: ",	event.offJet_phi[ event.caloJet_offmatch[i] ]
			print "offline csv: ", 			event.offJet_csv[  event.caloJet_offmatch[i] ]

                        if event.offJet_pt[  event.caloJet_offmatch[i] ] < 30 : continue

                        passed = False

			h_csv_inc_4Calo.Fill( 			event.offJet_csv[ event.caloJet_offmatch[i] ] )
                        if event.offJet_csv[ event.caloJet_offmatch[i] ] < 1. :
                            h_csv_inc_log_4Calo.Fill( 		-math.log( 1 -	event.offJet_csv[ event.caloJet_offmatch[i] ] ) )
			if SelectTrigger(event,triggerpath,False,"Calo",i) :
                                passed = True
				print "passes calo filter", event.offJet_csv[  event.caloJet_offmatch[i] ]
				h_csv_afcalo.Fill(			event.offJet_csv[ event.caloJet_offmatch[i] ] )
                                h_csv_inc_calo.Fill(                    event.offJet_csv[ event.caloJet_offmatch[i] ] )
                                if event.offJet_csv[ event.caloJet_offmatch[i] ] != 1. :
                                    h_csv_afcalo_log.Fill( 	-math.log( 1 - 	event.offJet_csv[ event.caloJet_offmatch[i] ] ) )	
                                    h_csv_inc_calo_log.Fill( -math.log( 1 -   event.offJet_csv[ event.caloJet_offmatch[i] ] ) )

                        eff_csv_inc_calo.Fill(passed, event.offJet_csv[ event.caloJet_offmatch[i] ] )
                        

	print "PF JET SECTION : # pf jet = ", event.pfJet_num
	for i in range(0, event.pfJet_num-1) :	
		if event.pfJet_offmatch[i] >= 0 :
			print "pf jet[", i, "]"
			print "event.pfJet_offmatch[i]: ", 	event.pfJet_offmatch[i], 	" event.offJet_num: ", 	event.offJet_num
			print "pf pt: ", 			event.pfJet_pt[i], 		" offline pt: ",	event.offJet_pt[  event.pfJet_offmatch[i] ]
			print "pf eta: ",			event.pfJet_eta[i],		" offline eta: ",	event.offJet_eta[ event.pfJet_offmatch[i] ]
			print "pf phi: ",			event.pfJet_phi[i],		" offline phi: ",	event.offJet_phi[ event.pfJet_offmatch[i] ]
			print "offline csv: ", 			event.offJet_csv[  event.pfJet_offmatch[i] ]

                        if event.offJet_pt[  event.pfJet_offmatch[i] ] < 30 : continue

                        passed = False

			h_csv_inc_4PF.Fill( 			event.offJet_csv[ event.pfJet_offmatch[i] ] )
                        if event.offJet_csv[ event.pfJet_offmatch[i] ] < 1. :
                            h_csv_inc_log_4PF.Fill( 		-math.log( 1 -	event.offJet_csv[ event.pfJet_offmatch[i] ] ) )
			if SelectTrigger(event,triggerpath,False,"PF",i) :
                                passed = True
				print "passes pf filter", event.offJet_csv[  event.pfJet_offmatch[i] ]
				h_csv_afpf.Fill(				event.offJet_csv[ event.pfJet_offmatch[i] ] )
				h_csv_inc_pf.Fill(				event.offJet_csv[ event.pfJet_offmatch[i] ] )
				h_csv_calo_pf.Fill(				event.offJet_csv[ event.pfJet_offmatch[i] ] )
                                if event.offJet_csv[ event.pfJet_offmatch[i] ] < 1. :
                                    h_csv_afpf_log.Fill( 	-math.log( 1 - 	event.offJet_csv[ event.pfJet_offmatch[i] ] ) )
                                    h_csv_inc_pf_log.Fill(	-math.log( 1 -  event.offJet_csv[ event.pfJet_offmatch[i] ] ) )
                                    h_csv_calo_pf_log.Fill(	-math.log( 1 -  event.offJet_csv[ event.pfJet_offmatch[i] ] ) )	

                        eff_csv_inc_pf.Fill(passed, event.offJet_csv[ event.pfJet_offmatch[i] ] )
                        if event.offJet_csv[ event.pfJet_offmatch[i] ] < 1. : eff_csv_inc_pf_log.Fill(passed, -math.log( 1 -  event.offJet_csv[ event.pfJet_offmatch[i] ] ) )


    f_results.Write()

####################################

main()
