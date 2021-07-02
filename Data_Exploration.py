{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "executionInfo": {
     "elapsed": 942,
     "status": "ok",
     "timestamp": 1623761918834,
     "user": {
      "displayName": "Sammie Kim",
      "photoUrl": "",
      "userId": "11393228328423561908"
     },
     "user_tz": 240
    },
    "id": "TCZaQ1WVeyTm",
    "outputId": "3c7cfcc8-ef69-4b35-aee6-34b5d4232593"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: python-docx in /usr/local/lib/python3.7/dist-packages (0.8.11)\n",
      "Requirement already satisfied: lxml>=2.3.2 in /usr/local/lib/python3.7/dist-packages (from python-docx) (4.2.6)\n",
      "Requirement already satisfied: nltk in /usr/local/lib/python3.7/dist-packages (3.2.5)\n",
      "Requirement already satisfied: six in /usr/local/lib/python3.7/dist-packages (from nltk) (1.15.0)\n"
     ]
    }
   ],
   "source": [
    "!pip install python-docx\n",
    "!pip install nltk"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "executionInfo": {
     "elapsed": 8925,
     "status": "ok",
     "timestamp": 1623761927699,
     "user": {
      "displayName": "Sammie Kim",
      "photoUrl": "",
      "userId": "11393228328423561908"
     },
     "user_tz": 240
    },
    "id": "TIjLDz-ZevDA",
    "outputId": "8372edee-c083-4627-a515-7f284c7c3c2f"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[nltk_data] Downloading package punkt to /root/nltk_data...\n",
      "[nltk_data]   Package punkt is already up-to-date!\n"
     ]
    }
   ],
   "source": [
    "import docx\n",
    "import nltk\n",
    "nltk.download('punkt')\n",
    "from nltk.tokenize import word_tokenize\n",
    "from nltk.tokenize import sent_tokenize\n",
    "import os\n",
    "import pickle\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import itertools"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "hZ_XtFWeF_x2"
   },
   "source": [
    "## Approach 1 - Convert Directly from PDF - issue with parsing"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "executionInfo": {
     "elapsed": 3986,
     "status": "ok",
     "timestamp": 1623320617609,
     "user": {
      "displayName": "Sammie Kim",
      "photoUrl": "",
      "userId": "11393228328423561908"
     },
     "user_tz": 240
    },
    "id": "wS_ArRJ2ZRzS",
    "outputId": "3b7bd570-4587-49e7-c498-fafc992204bc"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting PyPDF2\n",
      "\u001b[?25l  Downloading https://files.pythonhosted.org/packages/b4/01/68fcc0d43daf4c6bdbc6b33cc3f77bda531c86b174cac56ef0ffdb96faab/PyPDF2-1.26.0.tar.gz (77kB)\n",
      "\r",
      "\u001b[K     |████▎                           | 10kB 12.6MB/s eta 0:00:01\r",
      "\u001b[K     |████████▌                       | 20kB 16.8MB/s eta 0:00:01\r",
      "\u001b[K     |████████████▊                   | 30kB 19.1MB/s eta 0:00:01\r",
      "\u001b[K     |█████████████████               | 40kB 16.9MB/s eta 0:00:01\r",
      "\u001b[K     |█████████████████████▏          | 51kB 9.0MB/s eta 0:00:01\r",
      "\u001b[K     |█████████████████████████▍      | 61kB 10.2MB/s eta 0:00:01\r",
      "\u001b[K     |█████████████████████████████▋  | 71kB 9.3MB/s eta 0:00:01\r",
      "\u001b[K     |████████████████████████████████| 81kB 5.4MB/s \n",
      "\u001b[?25hBuilding wheels for collected packages: PyPDF2\n",
      "  Building wheel for PyPDF2 (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
      "  Created wheel for PyPDF2: filename=PyPDF2-1.26.0-cp37-none-any.whl size=61102 sha256=2213826b19178c74647993bbacfe8c6f8bf4664471a51934a81ed1697078fb88\n",
      "  Stored in directory: /root/.cache/pip/wheels/53/84/19/35bc977c8bf5f0c23a8a011aa958acd4da4bbd7a229315c1b7\n",
      "Successfully built PyPDF2\n",
      "Installing collected packages: PyPDF2\n",
      "Successfully installed PyPDF2-1.26.0\n"
     ]
    }
   ],
   "source": [
    "!pip install PyPDF2 \n",
    "!pip install pdfreader"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "executionInfo": {
     "elapsed": 7,
     "status": "ok",
     "timestamp": 1623320617610,
     "user": {
      "displayName": "Sammie Kim",
      "photoUrl": "",
      "userId": "11393228328423561908"
     },
     "user_tz": 240
    },
    "id": "aKv3AEbIZSKX"
   },
   "outputs": [],
   "source": [
    "import PyPDF2 as pdf"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "6syDFVfFZSNn"
   },
   "outputs": [],
   "source": [
    "file = open('/content/drive/MyDrive/Plagiarism/Whitepapers/0x.pdf', 'rb')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "UFP5TZbEZmw-"
   },
   "outputs": [],
   "source": [
    "pdf_reader = pdf.PdfFileReader(file)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 139
    },
    "executionInfo": {
     "elapsed": 451,
     "status": "ok",
     "timestamp": 1622546754244,
     "user": {
      "displayName": "Sammie Kim",
      "photoUrl": "",
      "userId": "11393228328423561908"
     },
     "user_tz": 240
    },
    "id": "Q7tG3zcCa6eK",
    "outputId": "80458164-8061-4f72-9265-9d7c58c36ed7"
   },
   "outputs": [
    {
     "data": {
      "application/vnd.google.colaboratory.intrinsic+json": {
       "type": "string"
      },
      "text/plain": [
       "\"1Introduction\\n\\nBlockchainshavebeenrevolutionarybyallowinganyonetoownandtran\\nsferassetsacrossanopennan-\\ncialnetworkwithouttheneedforatrustedthirdparty.Nowthatther\\nearehundreds[1]ofblockchain-\\nbasedassets,andmorebeingaddedeverymonth,theneedtoexchangeth\\neseassetsiscompounding.\\nWiththeadventofsmartcontracts,itispossiblefortwoormoreparties\\ntoexchangeblockchainassets\\nwithouttheneedforatrustedthirdparty.\\n\\nDecentralizedexchangeisanimportantprogressionfromtheecosystemof\\ncentralizedexchangesfora\\nfewkeyreasons:decentralizedexchangescanprovidestrongersecur\\nityguaranteestoenduserssince\\nthereisnolongeracentralpartywhichcanbehacked,runawaywithc\\nustomerfundsorbesubjectedto\\ngovernmentregulations.HacksofMt.Gox,ShapeshiftandBitnex[2,3]h\\navedemonstratedthatthese\\ntypesofsystemicrisksarepalpable.Decentralizedexchangewille\\nliminatetheserisksbyallowingusers\\ntotransacttrustlessly-withoutamiddleman-andbyplacingthebu\\nrdenofsecurityontoindividual\\nusersratherthanontoasinglecustodian.\\n\\nInthetwoyearsthathavepassedsincetheEthereumblockchain's\\ngenesisblock,numerousdecentralized\\napplications(dApps)havecreatedEthereumsmartcontractsforpeer-\\nto-peerexchange.Rapiditeration\\nandalackofbestpracticeshavelefttheblockchainscatteredwith\\nproprietaryandapplication-specic\\nimplementations.Asaresult,endusersareexposedtonumeroussmar\\ntcontractsofvaryingqualityand\\nsecurity,withuniquecongurationprocessesandlearningcurves\\n,allofwhichimplementthesamefunc-\\ntionality.Thisapproachimposesunecessarycostsonthenetworkbyfragm\\nentingendusersaccording\\ntotheparticulardAppeachuserhappenstobeusing,destroyingvalu\\nablenetworkeectsaroundliquidity.\\n0xisanopenprotocolfordecentralizedexchangeontheEthereumblockc\\nhain.Itisintendedtoserve\\nasabasicbuildingblockthatmaybecombinedwithotherprotocolsto\\ndriveincreasinglysophisticated\\ndApps[4].0xusesapubliclyaccessiblesystemofsmartcontractsthat\\ncanactassharedinfrastructure\\nforavarietyofdApps,asshowninFigure1.Inthelongrun,opentechnic\\nalstandardstendtowin\\noverclosedones,andasmoreassetsarebeingtokenizedontheblockchai\\nneachmonth,wewillseemore\\ndAppsthatrequiretheuseofthesedierenttokens.Asaresult,anop\\nenstandardforexchangeiscritical\\ntosupportingthisopeneconomy.\\nFigure1:Openprotocolsshouldbeapplication-agnostic.Decouplingthe\\nprotocollayerfromtheappli-\\ncationlayerprovidesmutualbenetsfordAppdevelopersandenduse\\nrsalike.\\n3\""
      ]
     },
     "execution_count": 6,
     "metadata": {
      "tags": []
     },
     "output_type": "execute_result"
    }
   ],
   "source": [
    "page1 = pdf_reader.getPage(2)\n",
    "page1.extractText()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "VpAopfePcDJ2"
   },
   "outputs": [],
   "source": [
    "file1 = open('/content/drive/MyDrive/Plagiarism/Whitepapers/Aave.pdf', 'rb')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "oAvlZRtXdK2v"
   },
   "outputs": [],
   "source": [
    "from pdfreader import SimplePDFViewer\n",
    "\n",
    "viewer = SimplePDFViewer(file1)\n",
    "viewer.render()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "page_0_content=viewer.canvas.text_content\n",
    "page_0_content\n",
    "\n",
    "# output\n",
    "#'\\n1 0 0 -1 0 843 cm\\n q\\n0 0 596 842.95715 re\\n W*\\n n\\n q\\n0.75062972 0 0 0.75062972 0 0 cm\\n1 1 1 RG\\n1 1 1 rg\\n/G3 gs\\n0 0 794 1123 re\\n f\\n0 0 794 1123 re\\n f\\n0 0 794 16845 re\\n f\\n0 0 794 1123 re\\n f\\n0 96 794 1027 re\\n f\\n96 111 602 25 re\\n f\\n96 135 602 40 re\\n f\\n96 174 602 35 re\\n f\\n96 208 602 35 re\\n f\\n96 242 602 20 re\\n f\\n96 261 602 20 re\\n f\\n96 280 602 20 re\\n f\\n96 299 602 35 re\\n f\\n96 333 602 20 re\\n f\\n96 352 602 20 re\\n f\\n120 401 578 20 re\\n f\\n120 420 578 20 re\\n f\\n168 439 530 20 re\\n f\\n168 458 530"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "Qm9QhihGlKkk"
   },
   "source": [
    "## Approach 2 - Convert from PDF to DOCX then sentence tokenization using NLTK "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "executionInfo": {
     "elapsed": 26,
     "status": "ok",
     "timestamp": 1623593216600,
     "user": {
      "displayName": "Sammie Kim",
      "photoUrl": "",
      "userId": "11393228328423561908"
     },
     "user_tz": 240
    },
    "id": "1WQsLM9_C-Eo"
   },
   "outputs": [],
   "source": [
    "# read docx as text\n",
    "def readtxt(filename):\n",
    "    doc = docx.Document(filename)\n",
    "    fullText = []\n",
    "    for para in doc.paragraphs:\n",
    "        fullText.append(para.text)\n",
    "    return '\\n'.join(fullText)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "executionInfo": {
     "elapsed": 275,
     "status": "ok",
     "timestamp": 1623071628726,
     "user": {
      "displayName": "Sammie Kim",
      "photoUrl": "",
      "userId": "11393228328423561908"
     },
     "user_tz": 240
    },
    "id": "oy8_3-ULm1YO",
    "outputId": "bd9b3ffd-a12a-4f75-8e2c-ee2c0097bc51"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "227\n",
      "209\n"
     ]
    }
   ],
   "source": [
    "# Raw vs. Lower result in different tokenized sentences\n",
    "tokenized_text_raw=sent_tokenize(readtxt('/content/drive/MyDrive/Plagiarism/Whitepapers_word/0x.docx'))\n",
    "tokenized_text_lower=sent_tokenize(readtxt('/content/drive/MyDrive/Plagiarism/Whitepapers_word/0x.docx').lower())\n",
    "\n",
    "print(len(tokenized_text_raw))\n",
    "print(len(tokenized_text_lower))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "1y1GEvxDm9BV"
   },
   "outputs": [],
   "source": [
    "# save a dictionary with Key: whitepaper name & Value: tokenized sentences both Raw and Lower in a tuple\n",
    "\n",
    "whitepaper_dict_ = {}\n",
    "folder = '/content/drive/MyDrive/Plagiarism/Whitepapers_word'\n",
    "for file in os.listdir(folder):\n",
    "  filepath = os.path.join(folder, file)\n",
    "  tokenized_text_raw = sent_tokenize(readtxt(filepath)) #need to do lower later\n",
    "  tokenized_text_lower = sent_tokenize(readtxt(filepath).lower())\n",
    "  whitepaper_dict_[file] = [tokenized_text_raw, tokenized_text_lower]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "Dnras2QjQUd4"
   },
   "outputs": [],
   "source": [
    "# save\n",
    "pickle.dump(whitepaper_dict_, open('/content/drive/MyDrive/Plagiarism/Whitepapers_txt/whitepaper_dict.pkl', 'wb'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "executionInfo": {
     "elapsed": 1541,
     "status": "ok",
     "timestamp": 1623432007416,
     "user": {
      "displayName": "Sammie Kim",
      "photoUrl": "",
      "userId": "11393228328423561908"
     },
     "user_tz": 240
    },
    "id": "M7yW4UoiQsiL"
   },
   "outputs": [],
   "source": [
    "# open\n",
    "whitepaper_dict = pickle.load(open('/content/drive/MyDrive/Plagiarism/Whitepapers_txt/whitepaper_dict.pkl', 'rb'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "executionInfo": {
     "elapsed": 295,
     "status": "ok",
     "timestamp": 1623082029819,
     "user": {
      "displayName": "Sammie Kim",
      "photoUrl": "",
      "userId": "11393228328423561908"
     },
     "user_tz": 240
    },
    "id": "tbhpICHiPfbl",
    "outputId": "08026acc-c54c-42cc-f3cc-401dd73b634e"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "342"
      ]
     },
     "execution_count": 35,
     "metadata": {
      "tags": []
     },
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(whitepaper_dict) # number of total whitepapers"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "executionInfo": {
     "elapsed": 13,
     "status": "ok",
     "timestamp": 1623073071955,
     "user": {
      "displayName": "Sammie Kim",
      "photoUrl": "",
      "userId": "11393228328423561908"
     },
     "user_tz": 240
    },
    "id": "u9K8-7FfPmlh",
    "outputId": "f56371a6-8676-4623-be9b-99cab6e4dce6"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "dict_keys(['ZVCHAIN.docx', 'Unibright.docx', 'Umbrella.docx', 'Waltonchain.docx', 'uniswap.docx', 'UTRUST.docx', 'THEKEY.docx', 'Telcoin.docx', 'Tron.docx', 'Vidy.docx', 'TomoChain.docx', 'TimeNewBank.docx', 'Tierion.docx', 'Theta-white-paper-latest.docx', 'TokenCard.docx', 'Tokenomy.docx', 'Tao.docx', 'Tap.docx', 'SwftCoin.docx', 'Sweetbridge.docx', 'Swarm.docx', 'Substratum.docx', 'SwissBorg.docx', 'Swipe.docx', 'Sport_and_Leisure.docx', 'SONM.docx', 'SmartMesh.docx', 'Streamr.docx', 'Storm.docx', 'Status.docx', 'StakeNet.docx', 'SALT.docx', 'Skale.docx', 'Singularity.docx', 'ShipChain.docx', 'SHIBA_INU.docx', 'SilentNotary.docx', 'shrimpy.docx', 'QunQun.docx', 'Silverway.docx', 'RequestNetwork.docx', 'RedFOX.docx', 'QASH.docx', 'ROONEX.docx', 'Qtum.docx', 'PowerLedger.docx', 'QuarkChain.docx', 'Propy.docx', 'PRIZM.docx', 'Polybius.docx', 'PolkaDotPaper.docx', 'dogecoin-whitepaper.docx', 'Aave.docx', 'AcuteAngleCould.docx', '0x.docx', 'Acala_Whitepaper.docx', 'aelf.docx', 'AgaveCoin.docx', 'Aeternity.docx', 'Aion.docx', 'AIOZ.docx', 'ADM_FinalProject.docx', 'Dropil.docx', 'Dusk.docx', 'Dragonchain.docx', 'Enigma.docx', 'Everus.docx', 'Everex.docx', 'Envion.docx', 'Edgeless.docx', 'Elastic.docx', 'Ethereum_original.docx', 'Elastos.docx', 'Ethos.docx', 'elrond-whitepaper.docx', 'Edgeware.docx', 'Entercoin.docx', 'Energo.docx', 'Electra.docx', 'Eximchain.docx', 'GreenPower.docx', 'Golem.docx', 'FeiProtocol.docx', 'FunctionX.docx', 'GNY.docx', 'Groestlcoin.docx', 'Gulden.docx', 'GridCoin.docx', 'IDEX.docx', 'Hegic.docx', 'HighPerformanceBlockchain.docx', 'HexxCoin.docx', 'Holo.docx', 'Hydra.docx', 'Ink.docx', 'IHTRealEstateProtocol.docx', 'InternetNodeToken.docx', 'IOStoken.docx', 'Iota.docx', 'IoTeX.docx', 'Karma.docx', 'Kylin.docx', 'Kyber.docx', 'Komodo.docx', 'Legolas.docx', 'Lamden.docx', 'Loki.docx', 'Lunyr.docx', 'Loopring.docx', 'LTONetwork.docx', 'Litex.docx', 'LiquidApps.docx', 'MaidSafeCoin.docx', 'MinexCoin.docx', 'MetaverseETP.docx', 'MakerDAO.docx', 'Mirror.docx', 'Mixin.docx', 'MicroBitcoin.docx', 'MAP.docx', 'MedicCoin.docx', 'MultiVAC.docx', 'Nectar.docx', 'NPCoin.docx', 'NKN.docx', 'NULS.docx', 'Nano.docx', 'Nebulas.docx', 'Nxt.docx', 'Numeraire.docx', 'Omisego.docx', 'Origo.docx', 'OriginTrail.docx', 'Orchid.docx', 'OST.docx', 'Pillar.docx', 'PIVX.docx', 'PayPie.docx', 'Paypex.docx', 'Peercoin.docx', 'pEOS.docx', 'Peerplays.docx', 'Paxos.docx', 'Perlin.docx', 'Populous.docx', 'PoseidonNetwork.docx', 'PlayFuel.docx', 'Polymath.docx', 'Primas.docx', 'ProjectPai.docx', 'QuantumResistantLedger.docx', 'Refereum.docx', 'Ripple.docx', 'RealTract.docx', 'Remme.docx', 'RocketPool.docx', 'Ravencoin.docx', 'ReddCoin.docx', 'SHIELD.docx', 'serum.docx', 'SelfSell.docx', 'shyft-network-inc-whitepaper_v4.1.docx', 'Shyft.docx', 'Selfkey.docx', 'Siacoin.docx', 'Skycoin.docx', 'Smartshare.docx', 'Steem.docx', 'Stellar.docx', 'SUN.docx', 'SunContract.docx', 'Syscoin.docx', 'SuperZero.docx', 'Terra.docx', 'Tigereum.docx', 'TheForceProtocol.docx', 'truefi.docx', 'Traxia.docx', 'truebit.docx', 'UNetwork.docx', 'Universa.docx', 'UNUS_SED_LEO.docx', 'Verge.docx', 'Viberate.docx', 'Viacoin.docx', 'Velas.docx', 'ULTRAIN.docx', 'VITE.docx', 'YOYOW.docx', 'WaykiChain.docx', 'Yee.docx', 'XinFin.docx', 'Zcash.docx', 'ZrCoin.docx', 'WazirX.docx', 'Waves.docx', 'Zebi.docx', 'WePower.docx', 'Wings.docx', 'Zilliqa.docx', 'XTRABYTES.docx', 'ZenCash.docx', 'ZEON.docx', 'Apex.docx', 'AllSports.docx', 'Ankr.docx', 'Ambrosus.docx', 'Akash.docx', 'Anoma.docx', 'ALQO.docx', 'APIS.docx', 'AMARK.docx', 'Alphacat.docx', 'Alchemix.docx', 'Ardor.docx', 'AtlasProtocol.docx', 'apM_Coin.docx', 'ArdCoin.docx', 'Ark.docx', 'Augur.docx', 'ApolloCurrency.docx', 'Audius.docx', 'AppCoins.docx', 'B2BX.docx', 'BABB.docx', 'Binance.docx', 'Bancor.docx', 'BitShares.docx', 'BitcoinStandardHashrateToken.docx', 'Bitspark.docx', 'BAND.docx', 'Blackmoon.docx', 'BeanCash.docx', 'BlockStamp.docx', 'Bitcoin.docx', 'Bankex.docx', 'Blocksafe.docx', 'BitbookGambling.docx', 'BlockMasonCreditProtocol.docx', 'Blocknet.docx', 'BAT.docx', 'BitcoinHD.docx', 'Boolberry.docx', 'Bodhi.docx', 'Blocktix.docx', 'Burst.docx', 'BOSAGORA.docx', 'Cardano.docx', 'CasinoCoin.docx', 'Bytom.docx', 'Bottos.docx', 'Cartesi.docx', 'Carry.docx', 'CEEKVR.docx', 'Bread.docx', 'BrahmaOS.docx', 'Bulwark.docx', 'BTUProtocol.docx', 'Centrality.docx', 'CelerNetwork-Whitepaper.docx', 'CertifiedDiamondNetwork.docx', 'Celer.docx', 'ChainGames.docx', 'ColossusXT.docx', 'Constellation.docx', 'Cook-Whitepaper-3.docx', 'CloakCoin.docx', 'Covesting.docx', 'CONUN.docx', 'CoinFLEX.docx', 'Cortex.docx', 'CoTrader.docx', 'Chia.docx', 'COSS.docx', 'Chronobank.docx', 'Cryptaur.docx', 'CyberVein.docx', 'Cryptonex.docx', 'CPChain.docx', 'Credits.docx', 'Crypterium.docx', 'Crust.docx', 'dKargo.docx', 'Dock.docx', 'DavinciCoin.docx', 'Datum.docx', 'Dai.docx', 'Darcrus.docx', 'Delphy.docx', 'DeepOnion.docx', 'Divi.docx', 'DMarket.docx', 'Dimecoin.docx', 'DigixDAO.docx', 'Dent.docx', 'Diamond.docx', 'PLATINCOIN.docx', 'Neblio.docx', 'PACcoin.docx', 'Nework.docx', 'N.Exchange.docx', 'Nucleus.docx', 'NoLimitCoin.docx', 'Nexo.docx', 'MediBloc.docx', 'Matrix.docx', 'MyBit.docx', 'NAGA.docx', 'Mobius.docx', 'Mithril.docx', 'Litentry.docx', 'LinkEye.docx', 'MovieBloc.docx', 'LunchMoney.docx', 'LuckySeven.docx', 'Levolution.docx', 'Lympo.docx', 'LUXCoin.docx', 'LINA.docx', 'lightning-white-paper.docx', 'LIFE.docx', 'KuCoin.docx', 'LindaCoin.docx', 'Kin.docx', 'INS.docx', 'Kleros.docx', 'Hshare.docx', 'Hifi_Finance.docx', 'Havven.docx', 'HTMLCOIN.docx', 'Icon.docx', 'GXChain.docx', 'INMAX.docx', 'GAPS.docx', 'Fusion.docx', 'FunFair.docx', 'GlitzKoin.docx', 'Gifto.docx', 'Grid+.docx', 'GoWithMi.docx', 'EXMR_FDN.docx', 'Egretia.docx'])\n"
     ]
    }
   ],
   "source": [
    "print(whitepaper_dict.keys()) # names of all whitepapers"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "0mW0BE0WoDaS"
   },
   "source": [
    "## Data Exploration"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "Vs9zr6rHoHUY"
   },
   "source": [
    "#### Number of sentences (segmented via NLTK) in each doc"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "executionInfo": {
     "elapsed": 218,
     "status": "ok",
     "timestamp": 1623321556795,
     "user": {
      "displayName": "Sammie Kim",
      "photoUrl": "",
      "userId": "11393228328423561908"
     },
     "user_tz": 240
    },
    "id": "bqdyDMEhOQRh"
   },
   "outputs": [],
   "source": [
    "# num of sentences in each doc for both raw and lower\n",
    "n_sentence_raw = []\n",
    "n_sentence_lower = []\n",
    "for key, values in whitepaper_dict.items():\n",
    "  n_sentence_raw.append(len(values[0]))\n",
    "  n_sentence_lower.append(len(values[1]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 0
    },
    "executionInfo": {
     "elapsed": 608,
     "status": "ok",
     "timestamp": 1623321768991,
     "user": {
      "displayName": "Sammie Kim",
      "photoUrl": "",
      "userId": "11393228328423561908"
     },
     "user_tz": 240
    },
    "id": "GaSbiS_ygNa0",
    "outputId": "eede4749-ba37-4839-b87c-755289db6905"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "number of documents 342\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light",
      "tags": []
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "print('number of documents', len(n_sentence_raw))\n",
    "\n",
    "plt.subplot(1, 2, 1)\n",
    "plt.hist(n_sentence_raw, bins=50)\n",
    "plt.title('number of sentences_raw')\n",
    "\n",
    "plt.subplot(1, 2, 2)\n",
    "plt.hist(n_sentence_lower, bins=50)\n",
    "plt.title('number of sentences_lower')\n",
    "\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "NiKo52IxQLyk"
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "_wmnmfqWpzqR"
   },
   "source": [
    "#### Check the sentence lengths (i.e., num of words in a sentence) for a few whitepapers. Word tokenization via NLTK."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "executionInfo": {
     "elapsed": 254,
     "status": "ok",
     "timestamp": 1622998855162,
     "user": {
      "displayName": "Sammie Kim",
      "photoUrl": "",
      "userId": "11393228328423561908"
     },
     "user_tz": 240
    },
    "id": "ZxTeLD9bQMLj",
    "outputId": "4ddbca8a-97c2-4c2b-8ed2-877284911e9d"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "22"
      ]
     },
     "execution_count": 26,
     "metadata": {
      "tags": []
     },
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(word_tokenize(whitepaper_dict1['dogecoin-whitepaper.docx'][1][0]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 0
    },
    "executionInfo": {
     "elapsed": 1390,
     "status": "ok",
     "timestamp": 1623322202089,
     "user": {
      "displayName": "Sammie Kim",
      "photoUrl": "",
      "userId": "11393228328423561908"
     },
     "user_tz": 240
    },
    "id": "w1g78QpkrciI",
    "outputId": "4ad8b335-9258-44c1-8f8c-2805839c4f7f"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Num of sentences for Doge: 44\n",
      "Avg sentence length for Doge: 23.022727272727273\n",
      "Num of sentences for Aave: 261\n",
      "Avg sentence length for Aave: 22.118773946360154\n",
      "Num of sentences for Acala: 186\n",
      "Avg sentence length for Acala: 32.13978494623656\n",
      "Num of sentences for Polkadot: 863\n",
      "Avg sentence length for Polkadot: 26.531865585168017\n",
      "-------------------\n",
      "Sentence Lengths\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 4 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light",
      "tags": []
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# comparison using lower case. y-axis is instances and x-axis is sentence lengths\n",
    "\n",
    "token_len_doge = [len(word_tokenize(i)) for i in whitepaper_dict['dogecoin-whitepaper.docx'][1]]\n",
    "token_len_aave = [len(word_tokenize(i)) for i in whitepaper_dict['Aave.docx'][1]]\n",
    "token_len_acala = [len(word_tokenize(i)) for i in whitepaper_dict['Acala_Whitepaper.docx'][1]]\n",
    "token_len_polkadot = [len(word_tokenize(i)) for i in whitepaper_dict['PolkaDotPaper.docx'][1]]\n",
    "\n",
    "print('Num of sentences for Doge:', len(token_len_doge)) \n",
    "print('Avg sentence length for Doge:', sum(token_len_doge) / len(token_len_doge))\n",
    "print('Num of sentences for Aave:', len(token_len_aave)) \n",
    "print('Avg sentence length for Aave:', sum(token_len_aave) / len(token_len_aave))\n",
    "print('Num of sentences for Acala:', len(token_len_acala)) \n",
    "print('Avg sentence length for Acala:', sum(token_len_acala) / len(token_len_acala))\n",
    "print('Num of sentences for Polkadot:', len(token_len_polkadot)) \n",
    "print('Avg sentence length for Polkadot:', sum(token_len_polkadot) / len(token_len_polkadot))\n",
    "\n",
    "print('-------------------') \n",
    "print('Sentence Lengths') \n",
    "\n",
    "plt.subplot(1, 4, 1)\n",
    "plt.hist(token_len_doge, bins=50)\n",
    "plt.title('Doge')\n",
    "\n",
    "plt.subplot(1, 4, 2)\n",
    "plt.hist(token_len_aave, bins=50)\n",
    "plt.title('Aave')\n",
    "\n",
    "plt.subplot(1, 4, 3)\n",
    "plt.hist(token_len_acala, bins=50)\n",
    "plt.title('Acala')\n",
    "\n",
    "plt.subplot(1, 4, 4)\n",
    "plt.hist(token_len_polkadot, bins=50)\n",
    "plt.title('Polkadot')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "executionInfo": {
     "elapsed": 197,
     "status": "ok",
     "timestamp": 1623322132502,
     "user": {
      "displayName": "Sammie Kim",
      "photoUrl": "",
      "userId": "11393228328423561908"
     },
     "user_tz": 240
    },
    "id": "kONTG9yniag5",
    "outputId": "8ff8fee6-8ec2-4242-836e-36b9bd42c2f8"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "23.022727272727273"
      ]
     },
     "execution_count": 22,
     "metadata": {
      "tags": []
     },
     "output_type": "execute_result"
    }
   ],
   "source": [
    "avg_value = sum(token_len_doge) / len(token_len_doge)\n",
    "avg_value\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "WSoUIzCiP9mT"
   },
   "source": [
    "Observations: \\\n",
    "(1) most of the sentence lengths are btw 0 and 50 -- > might need to remove sentence length below 5, etc.as there might be a parsing issue\n",
    "(2) sentence lengths > 50 should be looked at. probably not parsed correctly. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "YvJxJq8y3eJT"
   },
   "source": [
    "#### Check the mean & median sentence lengths"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {
    "executionInfo": {
     "elapsed": 219,
     "status": "ok",
     "timestamp": 1623323841677,
     "user": {
      "displayName": "Sammie Kim",
      "photoUrl": "",
      "userId": "11393228328423561908"
     },
     "user_tz": 240
    },
    "id": "k99O6uR1Tc-B"
   },
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {
    "executionInfo": {
     "elapsed": 18514,
     "status": "ok",
     "timestamp": 1623323861026,
     "user": {
      "displayName": "Sammie Kim",
      "photoUrl": "",
      "userId": "11393228328423561908"
     },
     "user_tz": 240
    },
    "id": "rj1XJgQjSykU"
   },
   "outputs": [],
   "source": [
    "mean_token_len = []\n",
    "median_token_len = []\n",
    "for key in whitepaper_dict.keys():\n",
    "  token_len = [len(word_tokenize(i)) for i in whitepaper_dict[key][1]]\n",
    "  median_token_len.append(np.percentile(np.array(token_len), 50))\n",
    "  mean_token_len.append(np.array(token_len).mean()) #mean sentence length for on document"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "executionInfo": {
     "elapsed": 372,
     "status": "ok",
     "timestamp": 1623083238329,
     "user": {
      "displayName": "Sammie Kim",
      "photoUrl": "",
      "userId": "11393228328423561908"
     },
     "user_tz": 240
    },
    "id": "c14W3vanTAGG",
    "outputId": "1eb07d8e-1316-47cd-a431-6ef0fa1ab561"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "52.925147449951666"
      ]
     },
     "execution_count": 46,
     "metadata": {
      "tags": []
     },
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.array(mean_token_len).mean() #mean sentence length across all documents"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 0
    },
    "executionInfo": {
     "elapsed": 415,
     "status": "ok",
     "timestamp": 1623323878364,
     "user": {
      "displayName": "Sammie Kim",
      "photoUrl": "",
      "userId": "11393228328423561908"
     },
     "user_tz": 240
    },
    "id": "VOTRuz_eThGd",
    "outputId": "887e823b-6bdc-43ac-92df-958a8577edb6"
   },
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light",
      "tags": []
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.hist(mean_token_len, bins=100)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 0
    },
    "executionInfo": {
     "elapsed": 414,
     "status": "ok",
     "timestamp": 1623323923688,
     "user": {
      "displayName": "Sammie Kim",
      "photoUrl": "",
      "userId": "11393228328423561908"
     },
     "user_tz": 240
    },
    "id": "38Qa_h9DRcsm",
    "outputId": "8e475c1b-2d55-4094-e775-3df85fa8f8b7"
   },
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light",
      "tags": []
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.hist(np.array(mean_token_len)[np.array(mean_token_len) < 200], bins = 50)  # mean seems to be around 25\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 265
    },
    "executionInfo": {
     "elapsed": 327,
     "status": "ok",
     "timestamp": 1623074314609,
     "user": {
      "displayName": "Sammie Kim",
      "photoUrl": "",
      "userId": "11393228328423561908"
     },
     "user_tz": 240
    },
    "id": "jmOoeWz-TpCz",
    "outputId": "9016259d-77c0-44c0-fd61-9e71051b020d"
   },
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light",
      "tags": []
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.hist(median_token_len)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "k41ImVgT3nLi"
   },
   "source": [
    "#### Check the frequency of words from all whitepapers"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "xHyrQae61Xdm"
   },
   "outputs": [],
   "source": [
    "vocab = {}\n",
    "for key in whitepaper_dict.keys():\n",
    "\n",
    "  token_len = [word_tokenize(i) for i in whitepaper_dict[key][1]]\n",
    "  for sent in token_len:\n",
    "    for word in sent:\n",
    "      try:\n",
    "        vocab[word] = vocab[word]+1\n",
    "      except:\n",
    "        vocab[word] = 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# the lowest frequency first\n",
    "vocab\n",
    "dict(sorted(vocab.items(), key=lambda item: item[1], reverse=False))\n",
    "\n",
    "## outcome\n",
    "# {'v0.4.6': 1,\n",
    "#  'pacers': 1,\n",
    "#  'encircled': 1,\n",
    "#  'majestic': 1,\n",
    "#  'behold': 1,\n",
    "#  'interclass': 1,\n",
    "#  '3000.': 1,\n",
    "#  'mundellian': 1,\n",
    "#  'function+boneh': 1,\n",
    "#  '-lynn': 1,\n",
    "#  '-shacham': 1,\n",
    "#  'in-form': 1,\n",
    "#  'complication': 1,\n",
    "#  'boneh–lynn–shacham': 1,\n",
    "#  'zkps': 1,\n",
    "#  'fractionated': 1,...}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# the highest frequency first\n",
    "vocab\n",
    "dict(sorted(vocab.items(), key=lambda item: item[1], reverse=True))\n",
    "\n",
    "## outcome\n",
    "# {'the': 158398,\n",
    "#  ',': 123900,\n",
    "#  '.': 108316,\n",
    "#  'of': 79718,\n",
    "#  'to': 72863,\n",
    "#  'and': 72257,\n",
    "#  'a': 56592,\n",
    "#  'in': 42992,\n",
    "#  'is': 37483,\n",
    "#  'for': 28416,\n",
    "#  'be': 22217,\n",
    "#  ')': 21261,\n",
    "#  '(': 21021,\n",
    "#  'that': 20967,\n",
    "#  'as': 19538,\n",
    "#  'on': 18504,\n",
    "#  'will': 17733,\n",
    "#  'with': 17444,\n",
    "#  'are': 16051,...}"
   ]
  }
 ],
 "metadata": {
  "colab": {
   "collapsed_sections": [
    "hZ_XtFWeF_x2",
    "Qm9QhihGlKkk",
    "0mW0BE0WoDaS",
    "njOvdbJUGFSj",
    "lylrHHIm4AQt",
    "AGUsOwbSA0nN",
    "FXDT4sb84cMy",
    "054Lc4fjBZNc",
    "UfcA6YiW49Is",
    "zfCVz4P5BtYI",
    "_QXaoXGf5K9F",
    "odfaeqqNANkT",
    "OaEs0m5GF4IY"
   ],
   "name": "Plagiarism.ipynb",
   "provenance": []
  },
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  },
  "widgets": {
   "application/vnd.jupyter.widget-state+json": {
    "0308a9a12d614147a3713cd797e6b6d1": {
     "model_module": "@jupyter-widgets/controls",
     "model_name": "DescriptionStyleModel",
     "state": {
      "_model_module": "@jupyter-widgets/controls",
      "_model_module_version": "1.5.0",
      "_model_name": "DescriptionStyleModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/base",
      "_view_module_version": "1.2.0",
      "_view_name": "StyleView",
      "description_width": ""
     }
    },
    "03c447b2cab94208b843eced6eca0d32": {
     "model_module": "@jupyter-widgets/controls",
     "model_name": "FloatProgressModel",
     "state": {
      "_dom_classes": [],
      "_model_module": "@jupyter-widgets/controls",
      "_model_module_version": "1.5.0",
      "_model_name": "FloatProgressModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/controls",
      "_view_module_version": "1.5.0",
      "_view_name": "ProgressView",
      "bar_style": "success",
      "description": "100%",
      "description_tooltip": null,
      "layout": "IPY_MODEL_e30b868f34864ab8957c09ea3b9fd88e",
      "max": 305249852,
      "min": 0,
      "orientation": "horizontal",
      "style": "IPY_MODEL_f5d185441c5b436682b2d91f381de705",
      "value": 305249852
     }
    },
    "0be8a138063e4281bd2222faa6429f4d": {
     "model_module": "@jupyter-widgets/controls",
     "model_name": "HTMLModel",
     "state": {
      "_dom_classes": [],
      "_model_module": "@jupyter-widgets/controls",
      "_model_module_version": "1.5.0",
      "_model_name": "HTMLModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/controls",
      "_view_module_version": "1.5.0",
      "_view_name": "HTMLView",
      "description": "",
      "description_tooltip": null,
      "layout": "IPY_MODEL_ba8b3c67df6740ed8fe65139fdc83ac1",
      "placeholder": "​",
      "style": "IPY_MODEL_583bbc2ec43f442c8b9f0a771083ac30",
      "value": " 405M/405M [00:34&lt;00:00, 11.8MB/s]"
     }
    },
    "0ca0f0ec27684efeb42cc13f741005ac": {
     "model_module": "@jupyter-widgets/base",
     "model_name": "LayoutModel",
     "state": {
      "_model_module": "@jupyter-widgets/base",
      "_model_module_version": "1.2.0",
      "_model_name": "LayoutModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/base",
      "_view_module_version": "1.2.0",
      "_view_name": "LayoutView",
      "align_content": null,
      "align_items": null,
      "align_self": null,
      "border": null,
      "bottom": null,
      "display": null,
      "flex": null,
      "flex_flow": null,
      "grid_area": null,
      "grid_auto_columns": null,
      "grid_auto_flow": null,
      "grid_auto_rows": null,
      "grid_column": null,
      "grid_gap": null,
      "grid_row": null,
      "grid_template_areas": null,
      "grid_template_columns": null,
      "grid_template_rows": null,
      "height": null,
      "justify_content": null,
      "justify_items": null,
      "left": null,
      "margin": null,
      "max_height": null,
      "max_width": null,
      "min_height": null,
      "min_width": null,
      "object_fit": null,
      "object_position": null,
      "order": null,
      "overflow": null,
      "overflow_x": null,
      "overflow_y": null,
      "padding": null,
      "right": null,
      "top": null,
      "visibility": null,
      "width": null
     }
    },
    "0f4588bf02b64f32b4c8bf2d948a90d4": {
     "model_module": "@jupyter-widgets/base",
     "model_name": "LayoutModel",
     "state": {
      "_model_module": "@jupyter-widgets/base",
      "_model_module_version": "1.2.0",
      "_model_name": "LayoutModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/base",
      "_view_module_version": "1.2.0",
      "_view_name": "LayoutView",
      "align_content": null,
      "align_items": null,
      "align_self": null,
      "border": null,
      "bottom": null,
      "display": null,
      "flex": null,
      "flex_flow": null,
      "grid_area": null,
      "grid_auto_columns": null,
      "grid_auto_flow": null,
      "grid_auto_rows": null,
      "grid_column": null,
      "grid_gap": null,
      "grid_row": null,
      "grid_template_areas": null,
      "grid_template_columns": null,
      "grid_template_rows": null,
      "height": null,
      "justify_content": null,
      "justify_items": null,
      "left": null,
      "margin": null,
      "max_height": null,
      "max_width": null,
      "min_height": null,
      "min_width": null,
      "object_fit": null,
      "object_position": null,
      "order": null,
      "overflow": null,
      "overflow_x": null,
      "overflow_y": null,
      "padding": null,
      "right": null,
      "top": null,
      "visibility": null,
      "width": null
     }
    },
    "0fbc0ea075604c4a87789c9f9f4020ba": {
     "model_module": "@jupyter-widgets/base",
     "model_name": "LayoutModel",
     "state": {
      "_model_module": "@jupyter-widgets/base",
      "_model_module_version": "1.2.0",
      "_model_name": "LayoutModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/base",
      "_view_module_version": "1.2.0",
      "_view_name": "LayoutView",
      "align_content": null,
      "align_items": null,
      "align_self": null,
      "border": null,
      "bottom": null,
      "display": null,
      "flex": null,
      "flex_flow": null,
      "grid_area": null,
      "grid_auto_columns": null,
      "grid_auto_flow": null,
      "grid_auto_rows": null,
      "grid_column": null,
      "grid_gap": null,
      "grid_row": null,
      "grid_template_areas": null,
      "grid_template_columns": null,
      "grid_template_rows": null,
      "height": null,
      "justify_content": null,
      "justify_items": null,
      "left": null,
      "margin": null,
      "max_height": null,
      "max_width": null,
      "min_height": null,
      "min_width": null,
      "object_fit": null,
      "object_position": null,
      "order": null,
      "overflow": null,
      "overflow_x": null,
      "overflow_y": null,
      "padding": null,
      "right": null,
      "top": null,
      "visibility": null,
      "width": null
     }
    },
    "19ba9f0f5431465faf5515e601993a13": {
     "model_module": "@jupyter-widgets/base",
     "model_name": "LayoutModel",
     "state": {
      "_model_module": "@jupyter-widgets/base",
      "_model_module_version": "1.2.0",
      "_model_name": "LayoutModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/base",
      "_view_module_version": "1.2.0",
      "_view_name": "LayoutView",
      "align_content": null,
      "align_items": null,
      "align_self": null,
      "border": null,
      "bottom": null,
      "display": null,
      "flex": null,
      "flex_flow": null,
      "grid_area": null,
      "grid_auto_columns": null,
      "grid_auto_flow": null,
      "grid_auto_rows": null,
      "grid_column": null,
      "grid_gap": null,
      "grid_row": null,
      "grid_template_areas": null,
      "grid_template_columns": null,
      "grid_template_rows": null,
      "height": null,
      "justify_content": null,
      "justify_items": null,
      "left": null,
      "margin": null,
      "max_height": null,
      "max_width": null,
      "min_height": null,
      "min_width": null,
      "object_fit": null,
      "object_position": null,
      "order": null,
      "overflow": null,
      "overflow_x": null,
      "overflow_y": null,
      "padding": null,
      "right": null,
      "top": null,
      "visibility": null,
      "width": null
     }
    },
    "1a07e8ff271c4725a8e7e7908b2f5157": {
     "model_module": "@jupyter-widgets/base",
     "model_name": "LayoutModel",
     "state": {
      "_model_module": "@jupyter-widgets/base",
      "_model_module_version": "1.2.0",
      "_model_name": "LayoutModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/base",
      "_view_module_version": "1.2.0",
      "_view_name": "LayoutView",
      "align_content": null,
      "align_items": null,
      "align_self": null,
      "border": null,
      "bottom": null,
      "display": null,
      "flex": null,
      "flex_flow": null,
      "grid_area": null,
      "grid_auto_columns": null,
      "grid_auto_flow": null,
      "grid_auto_rows": null,
      "grid_column": null,
      "grid_gap": null,
      "grid_row": null,
      "grid_template_areas": null,
      "grid_template_columns": null,
      "grid_template_rows": null,
      "height": null,
      "justify_content": null,
      "justify_items": null,
      "left": null,
      "margin": null,
      "max_height": null,
      "max_width": null,
      "min_height": null,
      "min_width": null,
      "object_fit": null,
      "object_position": null,
      "order": null,
      "overflow": null,
      "overflow_x": null,
      "overflow_y": null,
      "padding": null,
      "right": null,
      "top": null,
      "visibility": null,
      "width": null
     }
    },
    "1a9e9b221dce4ab2a25c286ef6b58f29": {
     "model_module": "@jupyter-widgets/controls",
     "model_name": "FloatProgressModel",
     "state": {
      "_dom_classes": [],
      "_model_module": "@jupyter-widgets/controls",
      "_model_module_version": "1.5.0",
      "_model_name": "FloatProgressModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/controls",
      "_view_module_version": "1.5.0",
      "_view_name": "ProgressView",
      "bar_style": "success",
      "description": "100%",
      "description_tooltip": null,
      "layout": "IPY_MODEL_6e0b09588ffa474ea007c75d13adbe56",
      "max": 122959036,
      "min": 0,
      "orientation": "horizontal",
      "style": "IPY_MODEL_f5b72290292948fcaca0faa95310428e",
      "value": 122959036
     }
    },
    "1f62f2bc4c984a9f9a02e4d4a86fb230": {
     "model_module": "@jupyter-widgets/base",
     "model_name": "LayoutModel",
     "state": {
      "_model_module": "@jupyter-widgets/base",
      "_model_module_version": "1.2.0",
      "_model_name": "LayoutModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/base",
      "_view_module_version": "1.2.0",
      "_view_name": "LayoutView",
      "align_content": null,
      "align_items": null,
      "align_self": null,
      "border": null,
      "bottom": null,
      "display": null,
      "flex": null,
      "flex_flow": null,
      "grid_area": null,
      "grid_auto_columns": null,
      "grid_auto_flow": null,
      "grid_auto_rows": null,
      "grid_column": null,
      "grid_gap": null,
      "grid_row": null,
      "grid_template_areas": null,
      "grid_template_columns": null,
      "grid_template_rows": null,
      "height": null,
      "justify_content": null,
      "justify_items": null,
      "left": null,
      "margin": null,
      "max_height": null,
      "max_width": null,
      "min_height": null,
      "min_width": null,
      "object_fit": null,
      "object_position": null,
      "order": null,
      "overflow": null,
      "overflow_x": null,
      "overflow_y": null,
      "padding": null,
      "right": null,
      "top": null,
      "visibility": null,
      "width": null
     }
    },
    "220e3b7c22764814ac3bd9b8796d6c9f": {
     "model_module": "@jupyter-widgets/controls",
     "model_name": "HTMLModel",
     "state": {
      "_dom_classes": [],
      "_model_module": "@jupyter-widgets/controls",
      "_model_module_version": "1.5.0",
      "_model_name": "HTMLModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/controls",
      "_view_module_version": "1.5.0",
      "_view_name": "HTMLView",
      "description": "",
      "description_tooltip": null,
      "layout": "IPY_MODEL_0ca0f0ec27684efeb42cc13f741005ac",
      "placeholder": "​",
      "style": "IPY_MODEL_7221d5114ab74a99964b168c8f71924c",
      "value": " 305M/305M [00:28&lt;00:00, 10.9MB/s]"
     }
    },
    "2343767b44b84485a49ee672502cb88c": {
     "model_module": "@jupyter-widgets/controls",
     "model_name": "HTMLModel",
     "state": {
      "_dom_classes": [],
      "_model_module": "@jupyter-widgets/controls",
      "_model_module_version": "1.5.0",
      "_model_name": "HTMLModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/controls",
      "_view_module_version": "1.5.0",
      "_view_name": "HTMLView",
      "description": "",
      "description_tooltip": null,
      "layout": "IPY_MODEL_1a07e8ff271c4725a8e7e7908b2f5157",
      "placeholder": "​",
      "style": "IPY_MODEL_e5270582915148a78cc9360ca1ef4b6e",
      "value": " 245M/245M [00:22&lt;00:00, 11.0MB/s]"
     }
    },
    "2445c6b7d10b407983120e20912a7fc0": {
     "model_module": "@jupyter-widgets/controls",
     "model_name": "HBoxModel",
     "state": {
      "_dom_classes": [],
      "_model_module": "@jupyter-widgets/controls",
      "_model_module_version": "1.5.0",
      "_model_name": "HBoxModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/controls",
      "_view_module_version": "1.5.0",
      "_view_name": "HBoxView",
      "box_style": "",
      "children": [
       "IPY_MODEL_03c447b2cab94208b843eced6eca0d32",
       "IPY_MODEL_aba0abe2c5714e42b06f4504b71a2e4f"
      ],
      "layout": "IPY_MODEL_19ba9f0f5431465faf5515e601993a13"
     }
    },
    "266b4cc7de764219a092b29b6e14cf8b": {
     "model_module": "@jupyter-widgets/controls",
     "model_name": "FloatProgressModel",
     "state": {
      "_dom_classes": [],
      "_model_module": "@jupyter-widgets/controls",
      "_model_module_version": "1.5.0",
      "_model_name": "FloatProgressModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/controls",
      "_view_module_version": "1.5.0",
      "_view_name": "ProgressView",
      "bar_style": "success",
      "description": "100%",
      "description_tooltip": null,
      "layout": "IPY_MODEL_a6163776cfad458b9637dce40f0bc87a",
      "max": 405057617,
      "min": 0,
      "orientation": "horizontal",
      "style": "IPY_MODEL_750724331c8b4a38ab434f3f8d0a5b96",
      "value": 405057617
     }
    },
    "2733e6e90f7b4fe28282017ea3b158e1": {
     "model_module": "@jupyter-widgets/controls",
     "model_name": "ProgressStyleModel",
     "state": {
      "_model_module": "@jupyter-widgets/controls",
      "_model_module_version": "1.5.0",
      "_model_name": "ProgressStyleModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/base",
      "_view_module_version": "1.2.0",
      "_view_name": "StyleView",
      "bar_color": null,
      "description_width": "initial"
     }
    },
    "29425bcc2cf54f6094ff06fdbc169cee": {
     "model_module": "@jupyter-widgets/base",
     "model_name": "LayoutModel",
     "state": {
      "_model_module": "@jupyter-widgets/base",
      "_model_module_version": "1.2.0",
      "_model_name": "LayoutModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/base",
      "_view_module_version": "1.2.0",
      "_view_name": "LayoutView",
      "align_content": null,
      "align_items": null,
      "align_self": null,
      "border": null,
      "bottom": null,
      "display": null,
      "flex": null,
      "flex_flow": null,
      "grid_area": null,
      "grid_auto_columns": null,
      "grid_auto_flow": null,
      "grid_auto_rows": null,
      "grid_column": null,
      "grid_gap": null,
      "grid_row": null,
      "grid_template_areas": null,
      "grid_template_columns": null,
      "grid_template_rows": null,
      "height": null,
      "justify_content": null,
      "justify_items": null,
      "left": null,
      "margin": null,
      "max_height": null,
      "max_width": null,
      "min_height": null,
      "min_width": null,
      "object_fit": null,
      "object_position": null,
      "order": null,
      "overflow": null,
      "overflow_x": null,
      "overflow_y": null,
      "padding": null,
      "right": null,
      "top": null,
      "visibility": null,
      "width": null
     }
    },
    "2ad4fa380ff1448bb26dc9db56448afd": {
     "model_module": "@jupyter-widgets/controls",
     "model_name": "HTMLModel",
     "state": {
      "_dom_classes": [],
      "_model_module": "@jupyter-widgets/controls",
      "_model_module_version": "1.5.0",
      "_model_name": "HTMLModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/controls",
      "_view_module_version": "1.5.0",
      "_view_name": "HTMLView",
      "description": "",
      "description_tooltip": null,
      "layout": "IPY_MODEL_29425bcc2cf54f6094ff06fdbc169cee",
      "placeholder": "​",
      "style": "IPY_MODEL_f35433de82e3476d9b41a1ad5801f672",
      "value": " 83.4M/83.4M [00:10&lt;00:00, 8.33MB/s]"
     }
    },
    "2ec3af1dfcef4b3db9b7d4bb7d063bd8": {
     "model_module": "@jupyter-widgets/base",
     "model_name": "LayoutModel",
     "state": {
      "_model_module": "@jupyter-widgets/base",
      "_model_module_version": "1.2.0",
      "_model_name": "LayoutModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/base",
      "_view_module_version": "1.2.0",
      "_view_name": "LayoutView",
      "align_content": null,
      "align_items": null,
      "align_self": null,
      "border": null,
      "bottom": null,
      "display": null,
      "flex": null,
      "flex_flow": null,
      "grid_area": null,
      "grid_auto_columns": null,
      "grid_auto_flow": null,
      "grid_auto_rows": null,
      "grid_column": null,
      "grid_gap": null,
      "grid_row": null,
      "grid_template_areas": null,
      "grid_template_columns": null,
      "grid_template_rows": null,
      "height": null,
      "justify_content": null,
      "justify_items": null,
      "left": null,
      "margin": null,
      "max_height": null,
      "max_width": null,
      "min_height": null,
      "min_width": null,
      "object_fit": null,
      "object_position": null,
      "order": null,
      "overflow": null,
      "overflow_x": null,
      "overflow_y": null,
      "padding": null,
      "right": null,
      "top": null,
      "visibility": null,
      "width": null
     }
    },
    "31612f1c66904100afcc9288a01cb849": {
     "model_module": "@jupyter-widgets/controls",
     "model_name": "HBoxModel",
     "state": {
      "_dom_classes": [],
      "_model_module": "@jupyter-widgets/controls",
      "_model_module_version": "1.5.0",
      "_model_name": "HBoxModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/controls",
      "_view_module_version": "1.5.0",
      "_view_name": "HBoxView",
      "box_style": "",
      "children": [
       "IPY_MODEL_9a74e2835e7848ffa1d3e53f0d93da78",
       "IPY_MODEL_220e3b7c22764814ac3bd9b8796d6c9f"
      ],
      "layout": "IPY_MODEL_0fbc0ea075604c4a87789c9f9f4020ba"
     }
    },
    "317c6c8fab424f3fb1ffc22bec47bcb0": {
     "model_module": "@jupyter-widgets/controls",
     "model_name": "ProgressStyleModel",
     "state": {
      "_model_module": "@jupyter-widgets/controls",
      "_model_module_version": "1.5.0",
      "_model_name": "ProgressStyleModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/base",
      "_view_module_version": "1.2.0",
      "_view_name": "StyleView",
      "bar_color": null,
      "description_width": "initial"
     }
    },
    "320b21927a2542bb8204e30ccaa920d8": {
     "model_module": "@jupyter-widgets/controls",
     "model_name": "HBoxModel",
     "state": {
      "_dom_classes": [],
      "_model_module": "@jupyter-widgets/controls",
      "_model_module_version": "1.5.0",
      "_model_name": "HBoxModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/controls",
      "_view_module_version": "1.5.0",
      "_view_name": "HBoxView",
      "box_style": "",
      "children": [
       "IPY_MODEL_7d09f39dd4f84511b99e22bb588e02dd",
       "IPY_MODEL_ce0b633b7e1e42d8a208e999dd0e814e"
      ],
      "layout": "IPY_MODEL_6aef8ca249b04b6c9113bcd3ff443436"
     }
    },
    "32bfaa66db144765b0dbaef25aa80c99": {
     "model_module": "@jupyter-widgets/base",
     "model_name": "LayoutModel",
     "state": {
      "_model_module": "@jupyter-widgets/base",
      "_model_module_version": "1.2.0",
      "_model_name": "LayoutModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/base",
      "_view_module_version": "1.2.0",
      "_view_name": "LayoutView",
      "align_content": null,
      "align_items": null,
      "align_self": null,
      "border": null,
      "bottom": null,
      "display": null,
      "flex": null,
      "flex_flow": null,
      "grid_area": null,
      "grid_auto_columns": null,
      "grid_auto_flow": null,
      "grid_auto_rows": null,
      "grid_column": null,
      "grid_gap": null,
      "grid_row": null,
      "grid_template_areas": null,
      "grid_template_columns": null,
      "grid_template_rows": null,
      "height": null,
      "justify_content": null,
      "justify_items": null,
      "left": null,
      "margin": null,
      "max_height": null,
      "max_width": null,
      "min_height": null,
      "min_width": null,
      "object_fit": null,
      "object_position": null,
      "order": null,
      "overflow": null,
      "overflow_x": null,
      "overflow_y": null,
      "padding": null,
      "right": null,
      "top": null,
      "visibility": null,
      "width": null
     }
    },
    "44f592713ec74e5cba4d8ddc0ff32e99": {
     "model_module": "@jupyter-widgets/controls",
     "model_name": "ProgressStyleModel",
     "state": {
      "_model_module": "@jupyter-widgets/controls",
      "_model_module_version": "1.5.0",
      "_model_name": "ProgressStyleModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/base",
      "_view_module_version": "1.2.0",
      "_view_name": "StyleView",
      "bar_color": null,
      "description_width": "initial"
     }
    },
    "45a86615870140fbbadabcb4067cc4e2": {
     "model_module": "@jupyter-widgets/controls",
     "model_name": "HBoxModel",
     "state": {
      "_dom_classes": [],
      "_model_module": "@jupyter-widgets/controls",
      "_model_module_version": "1.5.0",
      "_model_name": "HBoxModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/controls",
      "_view_module_version": "1.5.0",
      "_view_name": "HBoxView",
      "box_style": "",
      "children": [
       "IPY_MODEL_1a9e9b221dce4ab2a25c286ef6b58f29",
       "IPY_MODEL_47bc2c2a5f4f4de1964bfa596eae289b"
      ],
      "layout": "IPY_MODEL_5d73f81ed13040249ded851706974e8d"
     }
    },
    "462a455dded34a0f97aa1a84e926350b": {
     "model_module": "@jupyter-widgets/controls",
     "model_name": "DescriptionStyleModel",
     "state": {
      "_model_module": "@jupyter-widgets/controls",
      "_model_module_version": "1.5.0",
      "_model_name": "DescriptionStyleModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/base",
      "_view_module_version": "1.2.0",
      "_view_name": "StyleView",
      "description_width": ""
     }
    },
    "46fa45d8ee844d9396a74ebd58ece5bd": {
     "model_module": "@jupyter-widgets/base",
     "model_name": "LayoutModel",
     "state": {
      "_model_module": "@jupyter-widgets/base",
      "_model_module_version": "1.2.0",
      "_model_name": "LayoutModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/base",
      "_view_module_version": "1.2.0",
      "_view_name": "LayoutView",
      "align_content": null,
      "align_items": null,
      "align_self": null,
      "border": null,
      "bottom": null,
      "display": null,
      "flex": null,
      "flex_flow": null,
      "grid_area": null,
      "grid_auto_columns": null,
      "grid_auto_flow": null,
      "grid_auto_rows": null,
      "grid_column": null,
      "grid_gap": null,
      "grid_row": null,
      "grid_template_areas": null,
      "grid_template_columns": null,
      "grid_template_rows": null,
      "height": null,
      "justify_content": null,
      "justify_items": null,
      "left": null,
      "margin": null,
      "max_height": null,
      "max_width": null,
      "min_height": null,
      "min_width": null,
      "object_fit": null,
      "object_position": null,
      "order": null,
      "overflow": null,
      "overflow_x": null,
      "overflow_y": null,
      "padding": null,
      "right": null,
      "top": null,
      "visibility": null,
      "width": null
     }
    },
    "47bc2c2a5f4f4de1964bfa596eae289b": {
     "model_module": "@jupyter-widgets/controls",
     "model_name": "HTMLModel",
     "state": {
      "_dom_classes": [],
      "_model_module": "@jupyter-widgets/controls",
      "_model_module_version": "1.5.0",
      "_model_name": "HTMLModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/controls",
      "_view_module_version": "1.5.0",
      "_view_name": "HTMLView",
      "description": "",
      "description_tooltip": null,
      "layout": "IPY_MODEL_495cf0f556334915875b2da4823db908",
      "placeholder": "​",
      "style": "IPY_MODEL_5cbd0b5e4fbb4c7e9d1a9459973e92cc",
      "value": " 123M/123M [00:20&lt;00:00, 5.86MB/s]"
     }
    },
    "48b270bba7ed443f9cedc03cb1185b5f": {
     "model_module": "@jupyter-widgets/controls",
     "model_name": "DescriptionStyleModel",
     "state": {
      "_model_module": "@jupyter-widgets/controls",
      "_model_module_version": "1.5.0",
      "_model_name": "DescriptionStyleModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/base",
      "_view_module_version": "1.2.0",
      "_view_name": "StyleView",
      "description_width": ""
     }
    },
    "495cf0f556334915875b2da4823db908": {
     "model_module": "@jupyter-widgets/base",
     "model_name": "LayoutModel",
     "state": {
      "_model_module": "@jupyter-widgets/base",
      "_model_module_version": "1.2.0",
      "_model_name": "LayoutModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/base",
      "_view_module_version": "1.2.0",
      "_view_name": "LayoutView",
      "align_content": null,
      "align_items": null,
      "align_self": null,
      "border": null,
      "bottom": null,
      "display": null,
      "flex": null,
      "flex_flow": null,
      "grid_area": null,
      "grid_auto_columns": null,
      "grid_auto_flow": null,
      "grid_auto_rows": null,
      "grid_column": null,
      "grid_gap": null,
      "grid_row": null,
      "grid_template_areas": null,
      "grid_template_columns": null,
      "grid_template_rows": null,
      "height": null,
      "justify_content": null,
      "justify_items": null,
      "left": null,
      "margin": null,
      "max_height": null,
      "max_width": null,
      "min_height": null,
      "min_width": null,
      "object_fit": null,
      "object_position": null,
      "order": null,
      "overflow": null,
      "overflow_x": null,
      "overflow_y": null,
      "padding": null,
      "right": null,
      "top": null,
      "visibility": null,
      "width": null
     }
    },
    "562156be8c8b4af78d062efad671436b": {
     "model_module": "@jupyter-widgets/controls",
     "model_name": "HBoxModel",
     "state": {
      "_dom_classes": [],
      "_model_module": "@jupyter-widgets/controls",
      "_model_module_version": "1.5.0",
      "_model_name": "HBoxModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/controls",
      "_view_module_version": "1.5.0",
      "_view_name": "HBoxView",
      "box_style": "",
      "children": [
       "IPY_MODEL_b59bb7256a2548c6b3be6f5226cc1819",
       "IPY_MODEL_2ad4fa380ff1448bb26dc9db56448afd"
      ],
      "layout": "IPY_MODEL_1f62f2bc4c984a9f9a02e4d4a86fb230"
     }
    },
    "583bbc2ec43f442c8b9f0a771083ac30": {
     "model_module": "@jupyter-widgets/controls",
     "model_name": "DescriptionStyleModel",
     "state": {
      "_model_module": "@jupyter-widgets/controls",
      "_model_module_version": "1.5.0",
      "_model_name": "DescriptionStyleModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/base",
      "_view_module_version": "1.2.0",
      "_view_name": "StyleView",
      "description_width": ""
     }
    },
    "5cbd0b5e4fbb4c7e9d1a9459973e92cc": {
     "model_module": "@jupyter-widgets/controls",
     "model_name": "DescriptionStyleModel",
     "state": {
      "_model_module": "@jupyter-widgets/controls",
      "_model_module_version": "1.5.0",
      "_model_name": "DescriptionStyleModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/base",
      "_view_module_version": "1.2.0",
      "_view_name": "StyleView",
      "description_width": ""
     }
    },
    "5d73f81ed13040249ded851706974e8d": {
     "model_module": "@jupyter-widgets/base",
     "model_name": "LayoutModel",
     "state": {
      "_model_module": "@jupyter-widgets/base",
      "_model_module_version": "1.2.0",
      "_model_name": "LayoutModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/base",
      "_view_module_version": "1.2.0",
      "_view_name": "LayoutView",
      "align_content": null,
      "align_items": null,
      "align_self": null,
      "border": null,
      "bottom": null,
      "display": null,
      "flex": null,
      "flex_flow": null,
      "grid_area": null,
      "grid_auto_columns": null,
      "grid_auto_flow": null,
      "grid_auto_rows": null,
      "grid_column": null,
      "grid_gap": null,
      "grid_row": null,
      "grid_template_areas": null,
      "grid_template_columns": null,
      "grid_template_rows": null,
      "height": null,
      "justify_content": null,
      "justify_items": null,
      "left": null,
      "margin": null,
      "max_height": null,
      "max_width": null,
      "min_height": null,
      "min_width": null,
      "object_fit": null,
      "object_position": null,
      "order": null,
      "overflow": null,
      "overflow_x": null,
      "overflow_y": null,
      "padding": null,
      "right": null,
      "top": null,
      "visibility": null,
      "width": null
     }
    },
    "5fb46ac19ef94716b4157efb0db2ab9d": {
     "model_module": "@jupyter-widgets/base",
     "model_name": "LayoutModel",
     "state": {
      "_model_module": "@jupyter-widgets/base",
      "_model_module_version": "1.2.0",
      "_model_name": "LayoutModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/base",
      "_view_module_version": "1.2.0",
      "_view_name": "LayoutView",
      "align_content": null,
      "align_items": null,
      "align_self": null,
      "border": null,
      "bottom": null,
      "display": null,
      "flex": null,
      "flex_flow": null,
      "grid_area": null,
      "grid_auto_columns": null,
      "grid_auto_flow": null,
      "grid_auto_rows": null,
      "grid_column": null,
      "grid_gap": null,
      "grid_row": null,
      "grid_template_areas": null,
      "grid_template_columns": null,
      "grid_template_rows": null,
      "height": null,
      "justify_content": null,
      "justify_items": null,
      "left": null,
      "margin": null,
      "max_height": null,
      "max_width": null,
      "min_height": null,
      "min_width": null,
      "object_fit": null,
      "object_position": null,
      "order": null,
      "overflow": null,
      "overflow_x": null,
      "overflow_y": null,
      "padding": null,
      "right": null,
      "top": null,
      "visibility": null,
      "width": null
     }
    },
    "6aef8ca249b04b6c9113bcd3ff443436": {
     "model_module": "@jupyter-widgets/base",
     "model_name": "LayoutModel",
     "state": {
      "_model_module": "@jupyter-widgets/base",
      "_model_module_version": "1.2.0",
      "_model_name": "LayoutModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/base",
      "_view_module_version": "1.2.0",
      "_view_name": "LayoutView",
      "align_content": null,
      "align_items": null,
      "align_self": null,
      "border": null,
      "bottom": null,
      "display": null,
      "flex": null,
      "flex_flow": null,
      "grid_area": null,
      "grid_auto_columns": null,
      "grid_auto_flow": null,
      "grid_auto_rows": null,
      "grid_column": null,
      "grid_gap": null,
      "grid_row": null,
      "grid_template_areas": null,
      "grid_template_columns": null,
      "grid_template_rows": null,
      "height": null,
      "justify_content": null,
      "justify_items": null,
      "left": null,
      "margin": null,
      "max_height": null,
      "max_width": null,
      "min_height": null,
      "min_width": null,
      "object_fit": null,
      "object_position": null,
      "order": null,
      "overflow": null,
      "overflow_x": null,
      "overflow_y": null,
      "padding": null,
      "right": null,
      "top": null,
      "visibility": null,
      "width": null
     }
    },
    "6e0b09588ffa474ea007c75d13adbe56": {
     "model_module": "@jupyter-widgets/base",
     "model_name": "LayoutModel",
     "state": {
      "_model_module": "@jupyter-widgets/base",
      "_model_module_version": "1.2.0",
      "_model_name": "LayoutModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/base",
      "_view_module_version": "1.2.0",
      "_view_name": "LayoutView",
      "align_content": null,
      "align_items": null,
      "align_self": null,
      "border": null,
      "bottom": null,
      "display": null,
      "flex": null,
      "flex_flow": null,
      "grid_area": null,
      "grid_auto_columns": null,
      "grid_auto_flow": null,
      "grid_auto_rows": null,
      "grid_column": null,
      "grid_gap": null,
      "grid_row": null,
      "grid_template_areas": null,
      "grid_template_columns": null,
      "grid_template_rows": null,
      "height": null,
      "justify_content": null,
      "justify_items": null,
      "left": null,
      "margin": null,
      "max_height": null,
      "max_width": null,
      "min_height": null,
      "min_width": null,
      "object_fit": null,
      "object_position": null,
      "order": null,
      "overflow": null,
      "overflow_x": null,
      "overflow_y": null,
      "padding": null,
      "right": null,
      "top": null,
      "visibility": null,
      "width": null
     }
    },
    "7221d5114ab74a99964b168c8f71924c": {
     "model_module": "@jupyter-widgets/controls",
     "model_name": "DescriptionStyleModel",
     "state": {
      "_model_module": "@jupyter-widgets/controls",
      "_model_module_version": "1.5.0",
      "_model_name": "DescriptionStyleModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/base",
      "_view_module_version": "1.2.0",
      "_view_name": "StyleView",
      "description_width": ""
     }
    },
    "750724331c8b4a38ab434f3f8d0a5b96": {
     "model_module": "@jupyter-widgets/controls",
     "model_name": "ProgressStyleModel",
     "state": {
      "_model_module": "@jupyter-widgets/controls",
      "_model_module_version": "1.5.0",
      "_model_name": "ProgressStyleModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/base",
      "_view_module_version": "1.2.0",
      "_view_name": "StyleView",
      "bar_color": null,
      "description_width": "initial"
     }
    },
    "78542e3c5ad84ac2b3455419f644fbd4": {
     "model_module": "@jupyter-widgets/base",
     "model_name": "LayoutModel",
     "state": {
      "_model_module": "@jupyter-widgets/base",
      "_model_module_version": "1.2.0",
      "_model_name": "LayoutModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/base",
      "_view_module_version": "1.2.0",
      "_view_name": "LayoutView",
      "align_content": null,
      "align_items": null,
      "align_self": null,
      "border": null,
      "bottom": null,
      "display": null,
      "flex": null,
      "flex_flow": null,
      "grid_area": null,
      "grid_auto_columns": null,
      "grid_auto_flow": null,
      "grid_auto_rows": null,
      "grid_column": null,
      "grid_gap": null,
      "grid_row": null,
      "grid_template_areas": null,
      "grid_template_columns": null,
      "grid_template_rows": null,
      "height": null,
      "justify_content": null,
      "justify_items": null,
      "left": null,
      "margin": null,
      "max_height": null,
      "max_width": null,
      "min_height": null,
      "min_width": null,
      "object_fit": null,
      "object_position": null,
      "order": null,
      "overflow": null,
      "overflow_x": null,
      "overflow_y": null,
      "padding": null,
      "right": null,
      "top": null,
      "visibility": null,
      "width": null
     }
    },
    "7d09f39dd4f84511b99e22bb588e02dd": {
     "model_module": "@jupyter-widgets/controls",
     "model_name": "FloatProgressModel",
     "state": {
      "_dom_classes": [],
      "_model_module": "@jupyter-widgets/controls",
      "_model_module_version": "1.5.0",
      "_model_name": "FloatProgressModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/controls",
      "_view_module_version": "1.5.0",
      "_view_name": "ProgressView",
      "bar_style": "success",
      "description": "100%",
      "description_tooltip": null,
      "layout": "IPY_MODEL_b4190f7289be435098cca984e1f53194",
      "max": 305584576,
      "min": 0,
      "orientation": "horizontal",
      "style": "IPY_MODEL_317c6c8fab424f3fb1ffc22bec47bcb0",
      "value": 305584576
     }
    },
    "7ef5640e998e42b8bd7a52d82351a806": {
     "model_module": "@jupyter-widgets/base",
     "model_name": "LayoutModel",
     "state": {
      "_model_module": "@jupyter-widgets/base",
      "_model_module_version": "1.2.0",
      "_model_name": "LayoutModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/base",
      "_view_module_version": "1.2.0",
      "_view_name": "LayoutView",
      "align_content": null,
      "align_items": null,
      "align_self": null,
      "border": null,
      "bottom": null,
      "display": null,
      "flex": null,
      "flex_flow": null,
      "grid_area": null,
      "grid_auto_columns": null,
      "grid_auto_flow": null,
      "grid_auto_rows": null,
      "grid_column": null,
      "grid_gap": null,
      "grid_row": null,
      "grid_template_areas": null,
      "grid_template_columns": null,
      "grid_template_rows": null,
      "height": null,
      "justify_content": null,
      "justify_items": null,
      "left": null,
      "margin": null,
      "max_height": null,
      "max_width": null,
      "min_height": null,
      "min_width": null,
      "object_fit": null,
      "object_position": null,
      "order": null,
      "overflow": null,
      "overflow_x": null,
      "overflow_y": null,
      "padding": null,
      "right": null,
      "top": null,
      "visibility": null,
      "width": null
     }
    },
    "8dc87fb268984337953161e96b420779": {
     "model_module": "@jupyter-widgets/base",
     "model_name": "LayoutModel",
     "state": {
      "_model_module": "@jupyter-widgets/base",
      "_model_module_version": "1.2.0",
      "_model_name": "LayoutModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/base",
      "_view_module_version": "1.2.0",
      "_view_name": "LayoutView",
      "align_content": null,
      "align_items": null,
      "align_self": null,
      "border": null,
      "bottom": null,
      "display": null,
      "flex": null,
      "flex_flow": null,
      "grid_area": null,
      "grid_auto_columns": null,
      "grid_auto_flow": null,
      "grid_auto_rows": null,
      "grid_column": null,
      "grid_gap": null,
      "grid_row": null,
      "grid_template_areas": null,
      "grid_template_columns": null,
      "grid_template_rows": null,
      "height": null,
      "justify_content": null,
      "justify_items": null,
      "left": null,
      "margin": null,
      "max_height": null,
      "max_width": null,
      "min_height": null,
      "min_width": null,
      "object_fit": null,
      "object_position": null,
      "order": null,
      "overflow": null,
      "overflow_x": null,
      "overflow_y": null,
      "padding": null,
      "right": null,
      "top": null,
      "visibility": null,
      "width": null
     }
    },
    "966f3f990e674205a52275e8b5026993": {
     "model_module": "@jupyter-widgets/base",
     "model_name": "LayoutModel",
     "state": {
      "_model_module": "@jupyter-widgets/base",
      "_model_module_version": "1.2.0",
      "_model_name": "LayoutModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/base",
      "_view_module_version": "1.2.0",
      "_view_name": "LayoutView",
      "align_content": null,
      "align_items": null,
      "align_self": null,
      "border": null,
      "bottom": null,
      "display": null,
      "flex": null,
      "flex_flow": null,
      "grid_area": null,
      "grid_auto_columns": null,
      "grid_auto_flow": null,
      "grid_auto_rows": null,
      "grid_column": null,
      "grid_gap": null,
      "grid_row": null,
      "grid_template_areas": null,
      "grid_template_columns": null,
      "grid_template_rows": null,
      "height": null,
      "justify_content": null,
      "justify_items": null,
      "left": null,
      "margin": null,
      "max_height": null,
      "max_width": null,
      "min_height": null,
      "min_width": null,
      "object_fit": null,
      "object_position": null,
      "order": null,
      "overflow": null,
      "overflow_x": null,
      "overflow_y": null,
      "padding": null,
      "right": null,
      "top": null,
      "visibility": null,
      "width": null
     }
    },
    "9789e21b0a234a03bc84d94e5ff03679": {
     "model_module": "@jupyter-widgets/base",
     "model_name": "LayoutModel",
     "state": {
      "_model_module": "@jupyter-widgets/base",
      "_model_module_version": "1.2.0",
      "_model_name": "LayoutModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/base",
      "_view_module_version": "1.2.0",
      "_view_name": "LayoutView",
      "align_content": null,
      "align_items": null,
      "align_self": null,
      "border": null,
      "bottom": null,
      "display": null,
      "flex": null,
      "flex_flow": null,
      "grid_area": null,
      "grid_auto_columns": null,
      "grid_auto_flow": null,
      "grid_auto_rows": null,
      "grid_column": null,
      "grid_gap": null,
      "grid_row": null,
      "grid_template_areas": null,
      "grid_template_columns": null,
      "grid_template_rows": null,
      "height": null,
      "justify_content": null,
      "justify_items": null,
      "left": null,
      "margin": null,
      "max_height": null,
      "max_width": null,
      "min_height": null,
      "min_width": null,
      "object_fit": null,
      "object_position": null,
      "order": null,
      "overflow": null,
      "overflow_x": null,
      "overflow_y": null,
      "padding": null,
      "right": null,
      "top": null,
      "visibility": null,
      "width": null
     }
    },
    "98127b0842ec4591a3200dd430d24214": {
     "model_module": "@jupyter-widgets/controls",
     "model_name": "ProgressStyleModel",
     "state": {
      "_model_module": "@jupyter-widgets/controls",
      "_model_module_version": "1.5.0",
      "_model_name": "ProgressStyleModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/base",
      "_view_module_version": "1.2.0",
      "_view_name": "StyleView",
      "bar_color": null,
      "description_width": "initial"
     }
    },
    "9a74e2835e7848ffa1d3e53f0d93da78": {
     "model_module": "@jupyter-widgets/controls",
     "model_name": "FloatProgressModel",
     "state": {
      "_dom_classes": [],
      "_model_module": "@jupyter-widgets/controls",
      "_model_module_version": "1.5.0",
      "_model_name": "FloatProgressModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/controls",
      "_view_module_version": "1.5.0",
      "_view_name": "ProgressView",
      "bar_style": "success",
      "description": "100%",
      "description_tooltip": null,
      "layout": "IPY_MODEL_46fa45d8ee844d9396a74ebd58ece5bd",
      "max": 305249852,
      "min": 0,
      "orientation": "horizontal",
      "style": "IPY_MODEL_98127b0842ec4591a3200dd430d24214",
      "value": 305249852
     }
    },
    "9af39a50109047f5b8952d97781634dc": {
     "model_module": "@jupyter-widgets/controls",
     "model_name": "HTMLModel",
     "state": {
      "_dom_classes": [],
      "_model_module": "@jupyter-widgets/controls",
      "_model_module_version": "1.5.0",
      "_model_name": "HTMLModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/controls",
      "_view_module_version": "1.5.0",
      "_view_name": "HTMLView",
      "description": "",
      "description_tooltip": null,
      "layout": "IPY_MODEL_9789e21b0a234a03bc84d94e5ff03679",
      "placeholder": "​",
      "style": "IPY_MODEL_48b270bba7ed443f9cedc03cb1185b5f",
      "value": " 305M/305M [00:25&lt;00:00, 12.1MB/s]"
     }
    },
    "a0027000b0b64b0fbea6822258a7d4a9": {
     "model_module": "@jupyter-widgets/controls",
     "model_name": "ProgressStyleModel",
     "state": {
      "_model_module": "@jupyter-widgets/controls",
      "_model_module_version": "1.5.0",
      "_model_name": "ProgressStyleModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/base",
      "_view_module_version": "1.2.0",
      "_view_name": "StyleView",
      "bar_color": null,
      "description_width": "initial"
     }
    },
    "a6163776cfad458b9637dce40f0bc87a": {
     "model_module": "@jupyter-widgets/base",
     "model_name": "LayoutModel",
     "state": {
      "_model_module": "@jupyter-widgets/base",
      "_model_module_version": "1.2.0",
      "_model_name": "LayoutModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/base",
      "_view_module_version": "1.2.0",
      "_view_name": "LayoutView",
      "align_content": null,
      "align_items": null,
      "align_self": null,
      "border": null,
      "bottom": null,
      "display": null,
      "flex": null,
      "flex_flow": null,
      "grid_area": null,
      "grid_auto_columns": null,
      "grid_auto_flow": null,
      "grid_auto_rows": null,
      "grid_column": null,
      "grid_gap": null,
      "grid_row": null,
      "grid_template_areas": null,
      "grid_template_columns": null,
      "grid_template_rows": null,
      "height": null,
      "justify_content": null,
      "justify_items": null,
      "left": null,
      "margin": null,
      "max_height": null,
      "max_width": null,
      "min_height": null,
      "min_width": null,
      "object_fit": null,
      "object_position": null,
      "order": null,
      "overflow": null,
      "overflow_x": null,
      "overflow_y": null,
      "padding": null,
      "right": null,
      "top": null,
      "visibility": null,
      "width": null
     }
    },
    "aba0abe2c5714e42b06f4504b71a2e4f": {
     "model_module": "@jupyter-widgets/controls",
     "model_name": "HTMLModel",
     "state": {
      "_dom_classes": [],
      "_model_module": "@jupyter-widgets/controls",
      "_model_module_version": "1.5.0",
      "_model_name": "HTMLModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/controls",
      "_view_module_version": "1.5.0",
      "_view_name": "HTMLView",
      "description": "",
      "description_tooltip": null,
      "layout": "IPY_MODEL_78542e3c5ad84ac2b3455419f644fbd4",
      "placeholder": "​",
      "style": "IPY_MODEL_462a455dded34a0f97aa1a84e926350b",
      "value": " 305M/305M [00:20&lt;00:00, 14.7MB/s]"
     }
    },
    "b02afc39b49e44f7b298514c6df8ab36": {
     "model_module": "@jupyter-widgets/controls",
     "model_name": "HBoxModel",
     "state": {
      "_dom_classes": [],
      "_model_module": "@jupyter-widgets/controls",
      "_model_module_version": "1.5.0",
      "_model_name": "HBoxModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/controls",
      "_view_module_version": "1.5.0",
      "_view_name": "HBoxView",
      "box_style": "",
      "children": [
       "IPY_MODEL_266b4cc7de764219a092b29b6e14cf8b",
       "IPY_MODEL_0be8a138063e4281bd2222faa6429f4d"
      ],
      "layout": "IPY_MODEL_b35c2287211243608495d139a8513094"
     }
    },
    "b23a82b11c1841989fa7ddd8a45fabfc": {
     "model_module": "@jupyter-widgets/base",
     "model_name": "LayoutModel",
     "state": {
      "_model_module": "@jupyter-widgets/base",
      "_model_module_version": "1.2.0",
      "_model_name": "LayoutModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/base",
      "_view_module_version": "1.2.0",
      "_view_name": "LayoutView",
      "align_content": null,
      "align_items": null,
      "align_self": null,
      "border": null,
      "bottom": null,
      "display": null,
      "flex": null,
      "flex_flow": null,
      "grid_area": null,
      "grid_auto_columns": null,
      "grid_auto_flow": null,
      "grid_auto_rows": null,
      "grid_column": null,
      "grid_gap": null,
      "grid_row": null,
      "grid_template_areas": null,
      "grid_template_columns": null,
      "grid_template_rows": null,
      "height": null,
      "justify_content": null,
      "justify_items": null,
      "left": null,
      "margin": null,
      "max_height": null,
      "max_width": null,
      "min_height": null,
      "min_width": null,
      "object_fit": null,
      "object_position": null,
      "order": null,
      "overflow": null,
      "overflow_x": null,
      "overflow_y": null,
      "padding": null,
      "right": null,
      "top": null,
      "visibility": null,
      "width": null
     }
    },
    "b35c2287211243608495d139a8513094": {
     "model_module": "@jupyter-widgets/base",
     "model_name": "LayoutModel",
     "state": {
      "_model_module": "@jupyter-widgets/base",
      "_model_module_version": "1.2.0",
      "_model_name": "LayoutModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/base",
      "_view_module_version": "1.2.0",
      "_view_name": "LayoutView",
      "align_content": null,
      "align_items": null,
      "align_self": null,
      "border": null,
      "bottom": null,
      "display": null,
      "flex": null,
      "flex_flow": null,
      "grid_area": null,
      "grid_auto_columns": null,
      "grid_auto_flow": null,
      "grid_auto_rows": null,
      "grid_column": null,
      "grid_gap": null,
      "grid_row": null,
      "grid_template_areas": null,
      "grid_template_columns": null,
      "grid_template_rows": null,
      "height": null,
      "justify_content": null,
      "justify_items": null,
      "left": null,
      "margin": null,
      "max_height": null,
      "max_width": null,
      "min_height": null,
      "min_width": null,
      "object_fit": null,
      "object_position": null,
      "order": null,
      "overflow": null,
      "overflow_x": null,
      "overflow_y": null,
      "padding": null,
      "right": null,
      "top": null,
      "visibility": null,
      "width": null
     }
    },
    "b4190f7289be435098cca984e1f53194": {
     "model_module": "@jupyter-widgets/base",
     "model_name": "LayoutModel",
     "state": {
      "_model_module": "@jupyter-widgets/base",
      "_model_module_version": "1.2.0",
      "_model_name": "LayoutModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/base",
      "_view_module_version": "1.2.0",
      "_view_name": "LayoutView",
      "align_content": null,
      "align_items": null,
      "align_self": null,
      "border": null,
      "bottom": null,
      "display": null,
      "flex": null,
      "flex_flow": null,
      "grid_area": null,
      "grid_auto_columns": null,
      "grid_auto_flow": null,
      "grid_auto_rows": null,
      "grid_column": null,
      "grid_gap": null,
      "grid_row": null,
      "grid_template_areas": null,
      "grid_template_columns": null,
      "grid_template_rows": null,
      "height": null,
      "justify_content": null,
      "justify_items": null,
      "left": null,
      "margin": null,
      "max_height": null,
      "max_width": null,
      "min_height": null,
      "min_width": null,
      "object_fit": null,
      "object_position": null,
      "order": null,
      "overflow": null,
      "overflow_x": null,
      "overflow_y": null,
      "padding": null,
      "right": null,
      "top": null,
      "visibility": null,
      "width": null
     }
    },
    "b59bb7256a2548c6b3be6f5226cc1819": {
     "model_module": "@jupyter-widgets/controls",
     "model_name": "FloatProgressModel",
     "state": {
      "_dom_classes": [],
      "_model_module": "@jupyter-widgets/controls",
      "_model_module_version": "1.5.0",
      "_model_name": "FloatProgressModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/controls",
      "_view_module_version": "1.5.0",
      "_view_name": "ProgressView",
      "bar_style": "success",
      "description": "100%",
      "description_tooltip": null,
      "layout": "IPY_MODEL_2ec3af1dfcef4b3db9b7d4bb7d063bd8",
      "max": 83426730,
      "min": 0,
      "orientation": "horizontal",
      "style": "IPY_MODEL_bfdbef121f81461888f8851fafa8a617",
      "value": 83426730
     }
    },
    "ba8b3c67df6740ed8fe65139fdc83ac1": {
     "model_module": "@jupyter-widgets/base",
     "model_name": "LayoutModel",
     "state": {
      "_model_module": "@jupyter-widgets/base",
      "_model_module_version": "1.2.0",
      "_model_name": "LayoutModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/base",
      "_view_module_version": "1.2.0",
      "_view_name": "LayoutView",
      "align_content": null,
      "align_items": null,
      "align_self": null,
      "border": null,
      "bottom": null,
      "display": null,
      "flex": null,
      "flex_flow": null,
      "grid_area": null,
      "grid_auto_columns": null,
      "grid_auto_flow": null,
      "grid_auto_rows": null,
      "grid_column": null,
      "grid_gap": null,
      "grid_row": null,
      "grid_template_areas": null,
      "grid_template_columns": null,
      "grid_template_rows": null,
      "height": null,
      "justify_content": null,
      "justify_items": null,
      "left": null,
      "margin": null,
      "max_height": null,
      "max_width": null,
      "min_height": null,
      "min_width": null,
      "object_fit": null,
      "object_position": null,
      "order": null,
      "overflow": null,
      "overflow_x": null,
      "overflow_y": null,
      "padding": null,
      "right": null,
      "top": null,
      "visibility": null,
      "width": null
     }
    },
    "bfdbef121f81461888f8851fafa8a617": {
     "model_module": "@jupyter-widgets/controls",
     "model_name": "ProgressStyleModel",
     "state": {
      "_model_module": "@jupyter-widgets/controls",
      "_model_module_version": "1.5.0",
      "_model_name": "ProgressStyleModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/base",
      "_view_module_version": "1.2.0",
      "_view_name": "StyleView",
      "bar_color": null,
      "description_width": "initial"
     }
    },
    "c65114e90faa413ba01d7468a19fbda9": {
     "model_module": "@jupyter-widgets/controls",
     "model_name": "FloatProgressModel",
     "state": {
      "_dom_classes": [],
      "_model_module": "@jupyter-widgets/controls",
      "_model_module_version": "1.5.0",
      "_model_name": "FloatProgressModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/controls",
      "_view_module_version": "1.5.0",
      "_view_name": "ProgressView",
      "bar_style": "success",
      "description": "100%",
      "description_tooltip": null,
      "layout": "IPY_MODEL_b23a82b11c1841989fa7ddd8a45fabfc",
      "max": 305249852,
      "min": 0,
      "orientation": "horizontal",
      "style": "IPY_MODEL_2733e6e90f7b4fe28282017ea3b158e1",
      "value": 305249852
     }
    },
    "c86ab78dee6845799b35dc05da23bb83": {
     "model_module": "@jupyter-widgets/controls",
     "model_name": "FloatProgressModel",
     "state": {
      "_dom_classes": [],
      "_model_module": "@jupyter-widgets/controls",
      "_model_module_version": "1.5.0",
      "_model_name": "FloatProgressModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/controls",
      "_view_module_version": "1.5.0",
      "_view_name": "ProgressView",
      "bar_style": "success",
      "description": "100%",
      "description_tooltip": null,
      "layout": "IPY_MODEL_0f4588bf02b64f32b4c8bf2d948a90d4",
      "max": 244715968,
      "min": 0,
      "orientation": "horizontal",
      "style": "IPY_MODEL_44f592713ec74e5cba4d8ddc0ff32e99",
      "value": 244715968
     }
    },
    "ccd2285b10864c3e8c3e4020ca326451": {
     "model_module": "@jupyter-widgets/controls",
     "model_name": "DescriptionStyleModel",
     "state": {
      "_model_module": "@jupyter-widgets/controls",
      "_model_module_version": "1.5.0",
      "_model_name": "DescriptionStyleModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/base",
      "_view_module_version": "1.2.0",
      "_view_name": "StyleView",
      "description_width": ""
     }
    },
    "ce0b633b7e1e42d8a208e999dd0e814e": {
     "model_module": "@jupyter-widgets/controls",
     "model_name": "HTMLModel",
     "state": {
      "_dom_classes": [],
      "_model_module": "@jupyter-widgets/controls",
      "_model_module_version": "1.5.0",
      "_model_name": "HTMLModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/controls",
      "_view_module_version": "1.5.0",
      "_view_name": "HTMLView",
      "description": "",
      "description_tooltip": null,
      "layout": "IPY_MODEL_8dc87fb268984337953161e96b420779",
      "placeholder": "​",
      "style": "IPY_MODEL_0308a9a12d614147a3713cd797e6b6d1",
      "value": " 306M/306M [00:11&lt;00:00, 27.1MB/s]"
     }
    },
    "e1d60c75058343d8a61c4c1c3269daac": {
     "model_module": "@jupyter-widgets/controls",
     "model_name": "HTMLModel",
     "state": {
      "_dom_classes": [],
      "_model_module": "@jupyter-widgets/controls",
      "_model_module_version": "1.5.0",
      "_model_name": "HTMLModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/controls",
      "_view_module_version": "1.5.0",
      "_view_name": "HTMLView",
      "description": "",
      "description_tooltip": null,
      "layout": "IPY_MODEL_966f3f990e674205a52275e8b5026993",
      "placeholder": "​",
      "style": "IPY_MODEL_ccd2285b10864c3e8c3e4020ca326451",
      "value": " 306M/306M [00:39&lt;00:00, 7.78MB/s]"
     }
    },
    "e30b868f34864ab8957c09ea3b9fd88e": {
     "model_module": "@jupyter-widgets/base",
     "model_name": "LayoutModel",
     "state": {
      "_model_module": "@jupyter-widgets/base",
      "_model_module_version": "1.2.0",
      "_model_name": "LayoutModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/base",
      "_view_module_version": "1.2.0",
      "_view_name": "LayoutView",
      "align_content": null,
      "align_items": null,
      "align_self": null,
      "border": null,
      "bottom": null,
      "display": null,
      "flex": null,
      "flex_flow": null,
      "grid_area": null,
      "grid_auto_columns": null,
      "grid_auto_flow": null,
      "grid_auto_rows": null,
      "grid_column": null,
      "grid_gap": null,
      "grid_row": null,
      "grid_template_areas": null,
      "grid_template_columns": null,
      "grid_template_rows": null,
      "height": null,
      "justify_content": null,
      "justify_items": null,
      "left": null,
      "margin": null,
      "max_height": null,
      "max_width": null,
      "min_height": null,
      "min_width": null,
      "object_fit": null,
      "object_position": null,
      "order": null,
      "overflow": null,
      "overflow_x": null,
      "overflow_y": null,
      "padding": null,
      "right": null,
      "top": null,
      "visibility": null,
      "width": null
     }
    },
    "e4ca7fa71be848258aa4a4506206aba0": {
     "model_module": "@jupyter-widgets/base",
     "model_name": "LayoutModel",
     "state": {
      "_model_module": "@jupyter-widgets/base",
      "_model_module_version": "1.2.0",
      "_model_name": "LayoutModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/base",
      "_view_module_version": "1.2.0",
      "_view_name": "LayoutView",
      "align_content": null,
      "align_items": null,
      "align_self": null,
      "border": null,
      "bottom": null,
      "display": null,
      "flex": null,
      "flex_flow": null,
      "grid_area": null,
      "grid_auto_columns": null,
      "grid_auto_flow": null,
      "grid_auto_rows": null,
      "grid_column": null,
      "grid_gap": null,
      "grid_row": null,
      "grid_template_areas": null,
      "grid_template_columns": null,
      "grid_template_rows": null,
      "height": null,
      "justify_content": null,
      "justify_items": null,
      "left": null,
      "margin": null,
      "max_height": null,
      "max_width": null,
      "min_height": null,
      "min_width": null,
      "object_fit": null,
      "object_position": null,
      "order": null,
      "overflow": null,
      "overflow_x": null,
      "overflow_y": null,
      "padding": null,
      "right": null,
      "top": null,
      "visibility": null,
      "width": null
     }
    },
    "e5270582915148a78cc9360ca1ef4b6e": {
     "model_module": "@jupyter-widgets/controls",
     "model_name": "DescriptionStyleModel",
     "state": {
      "_model_module": "@jupyter-widgets/controls",
      "_model_module_version": "1.5.0",
      "_model_name": "DescriptionStyleModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/base",
      "_view_module_version": "1.2.0",
      "_view_name": "StyleView",
      "description_width": ""
     }
    },
    "e95f789e37a34bafb6a2491c4a1b8e48": {
     "model_module": "@jupyter-widgets/controls",
     "model_name": "FloatProgressModel",
     "state": {
      "_dom_classes": [],
      "_model_module": "@jupyter-widgets/controls",
      "_model_module_version": "1.5.0",
      "_model_name": "FloatProgressModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/controls",
      "_view_module_version": "1.5.0",
      "_view_name": "ProgressView",
      "bar_style": "success",
      "description": "100%",
      "description_tooltip": null,
      "layout": "IPY_MODEL_e4ca7fa71be848258aa4a4506206aba0",
      "max": 305584576,
      "min": 0,
      "orientation": "horizontal",
      "style": "IPY_MODEL_a0027000b0b64b0fbea6822258a7d4a9",
      "value": 305584576
     }
    },
    "ed2c5a85ebd547579874bb7d8d735cd0": {
     "model_module": "@jupyter-widgets/controls",
     "model_name": "HBoxModel",
     "state": {
      "_dom_classes": [],
      "_model_module": "@jupyter-widgets/controls",
      "_model_module_version": "1.5.0",
      "_model_name": "HBoxModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/controls",
      "_view_module_version": "1.5.0",
      "_view_name": "HBoxView",
      "box_style": "",
      "children": [
       "IPY_MODEL_c86ab78dee6845799b35dc05da23bb83",
       "IPY_MODEL_2343767b44b84485a49ee672502cb88c"
      ],
      "layout": "IPY_MODEL_7ef5640e998e42b8bd7a52d82351a806"
     }
    },
    "f35433de82e3476d9b41a1ad5801f672": {
     "model_module": "@jupyter-widgets/controls",
     "model_name": "DescriptionStyleModel",
     "state": {
      "_model_module": "@jupyter-widgets/controls",
      "_model_module_version": "1.5.0",
      "_model_name": "DescriptionStyleModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/base",
      "_view_module_version": "1.2.0",
      "_view_name": "StyleView",
      "description_width": ""
     }
    },
    "f5b72290292948fcaca0faa95310428e": {
     "model_module": "@jupyter-widgets/controls",
     "model_name": "ProgressStyleModel",
     "state": {
      "_model_module": "@jupyter-widgets/controls",
      "_model_module_version": "1.5.0",
      "_model_name": "ProgressStyleModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/base",
      "_view_module_version": "1.2.0",
      "_view_name": "StyleView",
      "bar_color": null,
      "description_width": "initial"
     }
    },
    "f5d185441c5b436682b2d91f381de705": {
     "model_module": "@jupyter-widgets/controls",
     "model_name": "ProgressStyleModel",
     "state": {
      "_model_module": "@jupyter-widgets/controls",
      "_model_module_version": "1.5.0",
      "_model_name": "ProgressStyleModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/base",
      "_view_module_version": "1.2.0",
      "_view_name": "StyleView",
      "bar_color": null,
      "description_width": "initial"
     }
    },
    "f83abaf51a4540a4ac1aef76bbfcba86": {
     "model_module": "@jupyter-widgets/controls",
     "model_name": "HBoxModel",
     "state": {
      "_dom_classes": [],
      "_model_module": "@jupyter-widgets/controls",
      "_model_module_version": "1.5.0",
      "_model_name": "HBoxModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/controls",
      "_view_module_version": "1.5.0",
      "_view_name": "HBoxView",
      "box_style": "",
      "children": [
       "IPY_MODEL_e95f789e37a34bafb6a2491c4a1b8e48",
       "IPY_MODEL_e1d60c75058343d8a61c4c1c3269daac"
      ],
      "layout": "IPY_MODEL_32bfaa66db144765b0dbaef25aa80c99"
     }
    },
    "fdf4f76891e4420485eef890388887d0": {
     "model_module": "@jupyter-widgets/controls",
     "model_name": "HBoxModel",
     "state": {
      "_dom_classes": [],
      "_model_module": "@jupyter-widgets/controls",
      "_model_module_version": "1.5.0",
      "_model_name": "HBoxModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/controls",
      "_view_module_version": "1.5.0",
      "_view_name": "HBoxView",
      "box_style": "",
      "children": [
       "IPY_MODEL_c65114e90faa413ba01d7468a19fbda9",
       "IPY_MODEL_9af39a50109047f5b8952d97781634dc"
      ],
      "layout": "IPY_MODEL_5fb46ac19ef94716b4157efb0db2ab9d"
     }
    }
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
