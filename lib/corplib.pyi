# Copyright(c) 2017 Charles University in Prague, Faculty of Arts,
#                   Institute of the Czech National Corpus
# Copyright(c) 2017 Tomas Machalek <tomas.machalek@gmail.com>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; version 2
# dated June, 1991.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

from typing import List, Any, Optional, Tuple, Dict
from manatee import Corpus, SubCorpus, Concordance, StrVector, PosAttr, Structure
import array.array

def manatee_version() -> str: ...

def manatee_min_version(ver:str) -> bool: ...

def open_corpus(*args:Any, **kwargs:Any) -> Corpus: ...

def create_subcorpus(path:str, corpus:Corpus, structname:str, subquery:str) -> SubCorpus: ...

def subcorpus_from_conc(path:str, conc:Concordance, struct:Optional[str]) -> SubCorpus: ...

def is_subcorpus(corp_obj:Corpus) -> bool: ...

def create_str_vector() -> StrVector: ...

def conf_bool(v:str) -> bool: ...

def add_block_items(items:Dict[str, Any], attr:Optional[str], val:Optional[str],
                    block_size:Optional[int]) -> Dict[str, Any]: ...

def get_wordlist_length(corp:Corpus, wlattr:str, wlpat:str, wlnums:str, wlminfreq:int, words:str,
                        blacklist:str, include_nonwords:bool): ...


def wordlist(corp:Corpus, words:Optional[List[str]], wlattr:Optional[str], wlpat:str, wlminfreq:int, wlmaxitems:int,
             wlsort:str, blacklist:Optional[List[str]], wlnums:Optional[str],
             include_nonwords:Optional[int]) -> Dict[str, Any]:...

def doc_sizes(corp:Corpus, struct:Structure, attrname:str, i:int, normvals:Dict[int, int]) -> int: ...

def texttype_values(corp:Corpus, subcorpattrs:str, maxlistsize:int, shrink_list:Optional[bool],
                    collator_locale:Optional[str]) -> List[Dict[str, Any]]: ...


def subc_freqs(subcorp:SubCorpus, attr:PosAttr, minfreq:Optional[int], maxfreq:Optional[int],
               last_id:Optional[int]) -> List[Tuple[int, int]]: ...

def subc_keywords(subcorp:SubCorpus, attr:PosAttr, minfreq:Optional[int], maxfreq:Optional[int],
                  last_id:Optional[int], maxitems:Optional[int]) -> Tuple[float, float, int, int]: ...

def subcorp_base_file(corp:SubCorpus, attrname:str) -> str: ...

def frq_db(corp:Corpus, attrname:str, nums:Optional[str], id_range:Optional[int]) -> array.array: ...

def subc_keywords_onstr(sc:SubCorpus, scref:SubCorpus, attrname:Optional[str], wlminfreq:Optional[int],
                        wlpat:Optional[str], wlmaxitems:Optional[int], simple_n:Optional[int],
                        wlwords:Optional[List[str]], blacklist:Optional[List[str]],
                        include_nonwords:Optional[int], wlnums:Optional[str]
                        ) -> Tuple[float, float, float, int, int, int, int, str]: ...

class CorpusManager(object):

    def default_subcpath(self, corp:Corpus) -> str: ...

    def get_Corpus(self, corpname:str, subcname:Optional[str]) -> Corpus: ...

    def findPosAttr(self, corpname:str, attrname:str) -> PosAttr: ...

    def corpconf_pairs(self, corp:Corpus, label:str) -> List[Tuple[str, str]]: ...

    def subc_files(self, corpname:str) -> List[str]: ...

    def subcorp_names(self, corpname:str) -> List[Dict[str, str]]: ...

