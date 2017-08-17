from launchNtupleFromAOD2017 import launchNtupleFromAOD2017

maxevents=50
# maxevents=50000
fileOutput = 'ntupleTest2017C_2017_08_17_50k.root'
filesInput=['root://cms-xrd-global.cern.ch//store/data/Run2017C/JetHT/AOD/PromptReco-v2/000/300/087/00000/0843AC55-0C77-E711-94BE-02163E01A5B8.root',
            'root://cms-xrd-global.cern.ch//store/data/Run2017C/JetHT/AOD/PromptReco-v2/000/300/087/00000/0C5B277D-0777-E711-B175-02163E01A5C1.root',
            'root://cms-xrd-global.cern.ch//store/data/Run2017C/JetHT/AOD/PromptReco-v2/000/300/087/00000/10D99DF8-0677-E711-9A7D-02163E01A302.root',
            'root://cms-xrd-global.cern.ch//store/data/Run2017C/JetHT/AOD/PromptReco-v2/000/300/087/00000/22ABF847-0577-E711-A8A5-02163E013446.root',
            'root://cms-xrd-global.cern.ch//store/data/Run2017C/JetHT/AOD/PromptReco-v2/000/300/087/00000/366BE27D-0277-E711-99D0-02163E011C8B.root',
            'root://cms-xrd-global.cern.ch//store/data/Run2017C/JetHT/AOD/PromptReco-v2/000/300/087/00000/56FFFA06-0777-E711-94B0-02163E01A3F6.root',
            'root://cms-xrd-global.cern.ch//store/data/Run2017C/JetHT/AOD/PromptReco-v2/000/300/087/00000/58870691-0A77-E711-B818-02163E019B72.root',
            'root://cms-xrd-global.cern.ch//store/data/Run2017C/JetHT/AOD/PromptReco-v2/000/300/087/00000/5A15B8D2-0E77-E711-897F-02163E0144A2.root',
            'root://cms-xrd-global.cern.ch//store/data/Run2017C/JetHT/AOD/PromptReco-v2/000/300/087/00000/60494131-1A77-E711-8A77-02163E014113.root',
            'root://cms-xrd-global.cern.ch//store/data/Run2017C/JetHT/AOD/PromptReco-v2/000/300/087/00000/660E42F6-0677-E711-99F7-02163E019D1D.root',
            'root://cms-xrd-global.cern.ch//store/data/Run2017C/JetHT/AOD/PromptReco-v2/000/300/087/00000/6A1372B2-1177-E711-B8B2-02163E0137A9.root',
            'root://cms-xrd-global.cern.ch//store/data/Run2017C/JetHT/AOD/PromptReco-v2/000/300/087/00000/74397C1F-0177-E711-944F-02163E019DA9.root',
            'root://cms-xrd-global.cern.ch//store/data/Run2017C/JetHT/AOD/PromptReco-v2/000/300/087/00000/78A0FA00-0477-E711-A206-02163E0146E0.root',
            'root://cms-xrd-global.cern.ch//store/data/Run2017C/JetHT/AOD/PromptReco-v2/000/300/087/00000/7A301E33-0377-E711-BCA3-02163E019DA9.root',
            'root://cms-xrd-global.cern.ch//store/data/Run2017C/JetHT/AOD/PromptReco-v2/000/300/087/00000/7EC11F8E-0C77-E711-956B-02163E01189C.root',
            'root://cms-xrd-global.cern.ch//store/data/Run2017C/JetHT/AOD/PromptReco-v2/000/300/087/00000/88DFE6A7-1277-E711-B5E4-02163E0119FA.root',
            'root://cms-xrd-global.cern.ch//store/data/Run2017C/JetHT/AOD/PromptReco-v2/000/300/087/00000/88EE9E2C-0877-E711-8A72-02163E011E56.root',
            'root://cms-xrd-global.cern.ch//store/data/Run2017C/JetHT/AOD/PromptReco-v2/000/300/087/00000/9A9B5E38-0577-E711-85A7-02163E01241E.root',
            'root://cms-xrd-global.cern.ch//store/data/Run2017C/JetHT/AOD/PromptReco-v2/000/300/087/00000/A06967CB-0877-E711-B0AC-02163E01A2B9.root',
            'root://cms-xrd-global.cern.ch//store/data/Run2017C/JetHT/AOD/PromptReco-v2/000/300/087/00000/B69D18A1-0F77-E711-9D39-02163E01A4E2.root',
            'root://cms-xrd-global.cern.ch//store/data/Run2017C/JetHT/AOD/PromptReco-v2/000/300/087/00000/C4B66555-0A77-E711-8EF4-02163E01A298.root',
            'root://cms-xrd-global.cern.ch//store/data/Run2017C/JetHT/AOD/PromptReco-v2/000/300/087/00000/CC9841EB-0377-E711-8F40-02163E01A6F6.root',
            'root://cms-xrd-global.cern.ch//store/data/Run2017C/JetHT/AOD/PromptReco-v2/000/300/087/00000/D86476C1-0777-E711-82D6-02163E019CDD.root',
            'root://cms-xrd-global.cern.ch//store/data/Run2017C/JetHT/AOD/PromptReco-v2/000/300/087/00000/E8D2EE93-0777-E711-85E7-02163E01A318.root',
            'root://cms-xrd-global.cern.ch//store/data/Run2017C/JetHT/AOD/PromptReco-v2/000/300/087/00000/F26E82AB-1077-E711-AE26-02163E01A589.root',
            'root://cms-xrd-global.cern.ch//store/data/Run2017C/JetHT/AOD/PromptReco-v2/000/300/087/00000/F6F20132-0577-E711-B559-02163E013825.root',
            'root://cms-xrd-global.cern.ch//store/data/Run2017C/JetHT/AOD/PromptReco-v2/000/300/101/00000/2AFA5DAF-0E77-E711-9AF1-02163E0143A0.root',
            'root://cms-xrd-global.cern.ch//store/data/Run2017C/JetHT/AOD/PromptReco-v2/000/300/104/00000/76AA58B5-1B77-E711-869C-02163E019C1F.root',
            'root://cms-xrd-global.cern.ch//store/data/Run2017C/JetHT/AOD/PromptReco-v2/000/300/105/00000/58047079-3B77-E711-BBB4-02163E019E63.root',
            'root://cms-xrd-global.cern.ch//store/data/Run2017C/JetHT/AOD/PromptReco-v2/000/300/106/00000/148755FD-3D77-E711-ADEF-02163E01A732.root',
            'root://cms-xrd-global.cern.ch//store/data/Run2017C/JetHT/AOD/PromptReco-v2/000/300/106/00000/20D97CBF-2377-E711-9278-02163E01A46D.root',
            'root://cms-xrd-global.cern.ch//store/data/Run2017C/JetHT/AOD/PromptReco-v2/000/300/106/00000/32F132F8-2D77-E711-B797-02163E01A49A.root',
            'root://cms-xrd-global.cern.ch//store/data/Run2017C/JetHT/AOD/PromptReco-v2/000/300/106/00000/3A4D0093-2F77-E711-878A-02163E019E8B.root',
            'root://cms-xrd-global.cern.ch//store/data/Run2017C/JetHT/AOD/PromptReco-v2/000/300/106/00000/46AECA86-3177-E711-A61F-02163E013496.root',
            'root://cms-xrd-global.cern.ch//store/data/Run2017C/JetHT/AOD/PromptReco-v2/000/300/106/00000/74558817-2C77-E711-B6F4-02163E0128AB.root',
            'root://cms-xrd-global.cern.ch//store/data/Run2017C/JetHT/AOD/PromptReco-v2/000/300/106/00000/80697259-3577-E711-A488-02163E01240B.root',
            'root://cms-xrd-global.cern.ch//store/data/Run2017C/JetHT/AOD/PromptReco-v2/000/300/106/00000/86DDF7B9-3477-E711-A1D1-02163E01A20B.root',
            'root://cms-xrd-global.cern.ch//store/data/Run2017C/JetHT/AOD/PromptReco-v2/000/300/106/00000/AAD7244B-3077-E711-BB0F-02163E011CBF.root',
            'root://cms-xrd-global.cern.ch//store/data/Run2017C/JetHT/AOD/PromptReco-v2/000/300/106/00000/ACD6341F-2877-E711-8E4F-02163E01A3DC.root',
            'root://cms-xrd-global.cern.ch//store/data/Run2017C/JetHT/AOD/PromptReco-v2/000/300/106/00000/B4ACE520-3377-E711-B37D-02163E014736.root',
            'root://cms-xrd-global.cern.ch//store/data/Run2017C/JetHT/AOD/PromptReco-v2/000/300/106/00000/C245AD09-3B77-E711-82E6-02163E019CC4.root',
            'root://cms-xrd-global.cern.ch//store/data/Run2017C/JetHT/AOD/PromptReco-v2/000/300/106/00000/C45F263E-2B77-E711-A9DC-02163E014236.root',
            'root://cms-xrd-global.cern.ch//store/data/Run2017C/JetHT/AOD/PromptReco-v2/000/300/106/00000/D80DDB21-2B77-E711-8A1E-02163E0134E2.root',
            'root://cms-xrd-global.cern.ch//store/data/Run2017C/JetHT/AOD/PromptReco-v2/000/300/106/00000/E62B2B10-2F77-E711-861F-02163E014198.root',
            'root://cms-xrd-global.cern.ch//store/data/Run2017C/JetHT/AOD/PromptReco-v2/000/300/106/00000/E8029457-2877-E711-A921-02163E01A23B.root',
            'root://cms-xrd-global.cern.ch//store/data/Run2017C/JetHT/AOD/PromptReco-v2/000/300/107/00000/02A82948-2977-E711-956E-02163E01190B.root',
            'root://cms-xrd-global.cern.ch//store/data/Run2017C/JetHT/AOD/PromptReco-v2/000/300/107/00000/445B3CDC-2D77-E711-B1BE-02163E01A2B3.root',
            'root://cms-xrd-global.cern.ch//store/data/Run2017C/JetHT/AOD/PromptReco-v2/000/300/107/00000/46DA28BA-2877-E711-AA43-02163E019CE4.root',
            'root://cms-xrd-global.cern.ch//store/data/Run2017C/JetHT/AOD/PromptReco-v2/000/300/107/00000/60F2E1F8-3A77-E711-B76A-02163E01A3E5.root',
            'root://cms-xrd-global.cern.ch//store/data/Run2017C/JetHT/AOD/PromptReco-v2/000/300/107/00000/66C669D7-3177-E711-B297-02163E01A355.root',
            'root://cms-xrd-global.cern.ch//store/data/Run2017C/JetHT/AOD/PromptReco-v2/000/300/107/00000/78B339F9-2C77-E711-BCA2-02163E01A35F.root',
            'root://cms-xrd-global.cern.ch//store/data/Run2017C/JetHT/AOD/PromptReco-v2/000/300/107/00000/9690D273-3777-E711-AB22-02163E011DEE.root',
            'root://cms-xrd-global.cern.ch//store/data/Run2017C/JetHT/AOD/PromptReco-v2/000/300/107/00000/9C763924-3477-E711-B199-02163E01A403.root',
            'root://cms-xrd-global.cern.ch//store/data/Run2017C/JetHT/AOD/PromptReco-v2/000/300/107/00000/A84E01D6-3577-E711-BD08-02163E01A1B7.root',
            'root://cms-xrd-global.cern.ch//store/data/Run2017C/JetHT/AOD/PromptReco-v2/000/300/107/00000/CAA4518C-3477-E711-A035-02163E0141FB.root',
            'root://cms-xrd-global.cern.ch//store/data/Run2017C/JetHT/AOD/PromptReco-v2/000/300/107/00000/F2FDA45F-3277-E711-B262-02163E01A2B3.root',
            'root://cms-xrd-global.cern.ch//store/data/Run2017C/JetHT/AOD/PromptReco-v2/000/300/107/00000/F6D3A0C0-2377-E711-B799-02163E01441A.root',
            'root://cms-xrd-global.cern.ch//store/data/Run2017C/JetHT/AOD/PromptReco-v2/000/300/117/00000/14062050-4777-E711-A965-02163E011DE8.root',
            'root://cms-xrd-global.cern.ch//store/data/Run2017C/JetHT/AOD/PromptReco-v2/000/300/117/00000/1E4381EC-3977-E711-AD06-02163E01A5DC.root',
            'root://cms-xrd-global.cern.ch//store/data/Run2017C/JetHT/AOD/PromptReco-v2/000/300/117/00000/809EC2D7-4077-E711-9691-02163E01A6B2.root',
            'root://cms-xrd-global.cern.ch//store/data/Run2017C/JetHT/AOD/PromptReco-v2/000/300/117/00000/CAD0FF3F-2E77-E711-B9A4-02163E019D0F.root',
            'root://cms-xrd-global.cern.ch//store/data/Run2017C/JetHT/AOD/PromptReco-v2/000/300/117/00000/EA21C23B-3677-E711-8B2B-02163E01A302.root'
            ]
launchNtupleFromAOD2017(fileOutput,filesInput,maxevents)
