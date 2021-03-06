import FWCore.ParameterSet.Config as cms

from XiAnalyzer.XiAnalyzer.matchselector_cfi import *

MatchCandidatesKshort = MatchCandidates.clone()

MatchCandidatesLambda = MatchCandidates.clone(
        v0IDName = cms.string('Lambda'),
        gnV0Collection = cms.InputTag('selectGenCandidatesLambda:Lambda')
        )
