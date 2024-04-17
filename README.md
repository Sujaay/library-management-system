# IIT-M BS APP DEV - 1 Project
## Library Managament System

### To Create virtual environment
- For linux `python3 -m venv .env`
- For windows `python -m venv .env`

### To activate virtual environment
- For linux `source .env/bin/activate`
- For windows `.\.env\Scripts\activate`

### To run the application
- For linux `python3 app.py`
- For windows `python app.py`




```
library management system
├─ .gitignore
├─ add_data.py
├─ app.py
├─ application
│  ├─ database.py
│  ├─ models.py
│  ├─ routes.py
│  ├─ variables.py
│  ├─ __init__.py
│  └─ __pycache__
│     ├─ database.cpython-311.pyc
│     ├─ models.cpython-311.pyc
│     ├─ routes.cpython-311.pyc
│     └─ __init__.cpython-311.pyc
├─ components
│  ├─ Footer.html
│  └─ navbar.html
├─ instance
│  └─ database.sqlite3
├─ README.md
├─ requirements.txt
├─ static
│  ├─ favicon.ico
│  ├─ librarian_dashboard.css
│  ├─ librarian_nav.css
│  ├─ library_statistics.css
│  ├─ login.css
│  └─ register.css
├─ templates
│  ├─ index.html
│  ├─ librarian
│  │  ├─ book
│  │  │  ├─ add.html
│  │  │  ├─ delete.html
│  │  │  └─ edit.html
│  │  ├─ librarian_dashboard.html
│  │  ├─ library_statistics.html
│  │  └─ section
│  │     ├─ add_section.html
│  │     ├─ books.html
│  │     └─ sections.html
│  ├─ login.html
│  ├─ register.html
│  ├─ user_account_settings.html
│  ├─ user_browse_sections.html
│  ├─ user_dashboard.html
│  └─ user_my_books.html
└─ __pycache__
   └─ app.cpython-311.pyc

```
```
library management system
├─ .git
│  ├─ COMMIT_EDITMSG
│  ├─ config
│  ├─ description
│  ├─ FETCH_HEAD
│  ├─ HEAD
│  ├─ hooks
│  │  ├─ applypatch-msg.sample
│  │  ├─ commit-msg.sample
│  │  ├─ fsmonitor-watchman.sample
│  │  ├─ post-update.sample
│  │  ├─ pre-applypatch.sample
│  │  ├─ pre-commit.sample
│  │  ├─ pre-merge-commit.sample
│  │  ├─ pre-push.sample
│  │  ├─ pre-rebase.sample
│  │  ├─ pre-receive.sample
│  │  ├─ prepare-commit-msg.sample
│  │  ├─ push-to-checkout.sample
│  │  ├─ sendemail-validate.sample
│  │  └─ update.sample
│  ├─ index
│  ├─ info
│  │  └─ exclude
│  ├─ logs
│  │  ├─ HEAD
│  │  └─ refs
│  │     ├─ heads
│  │     │  └─ master
│  │     └─ remotes
│  │        └─ origin
│  │           └─ master
│  ├─ objects
│  │  ├─ 00
│  │  │  ├─ 2ec4141f748b363a9cda2f8b2466c85d855022
│  │  │  ├─ 58a6941e3c604ba12316776d8e70b4f9a58a4b
│  │  │  └─ 74ddbf7e3a4b8edd3749a8f956f1261cc8fefb
│  │  ├─ 02
│  │  │  ├─ 016ef66acb56754d4ca46e455fad11a77a3127
│  │  │  └─ 8ffbd3688908f08c0bcef8e3a228c5f3562ad1
│  │  ├─ 03
│  │  │  ├─ 42e1f85466ebfc93aebd718b1ba5e2f14839bf
│  │  │  ├─ b9e9f4df6dd3835677ac47f37d65530330443b
│  │  │  └─ bb6fbe8114a97b3f64df7856c232079a8c2406
│  │  ├─ 04
│  │  │  └─ 63472e9412d67ed1e606f88c71b57a5ad78ee3
│  │  ├─ 06
│  │  │  ├─ 3e340a2d2965894287aaa1806595c592996338
│  │  │  ├─ a355dee2c66981ee8475247c09dd0d260beecf
│  │  │  └─ f82ea450909cd05062a583ca59feef4b48e9ce
│  │  ├─ 07
│  │  │  ├─ b9db228ac993cdc6670a93a9b07ef724878945
│  │  │  └─ e63565435eaa9d7aba752cf410d7592b112bdf
│  │  ├─ 08
│  │  │  ├─ 13f1b881a9afdc839c88df1ae96ca75b4796af
│  │  │  ├─ 3d333d444112da36cb0cf7fd1fd5ec44548929
│  │  │  └─ 755508158d3d0833bb4b2f77b2711fa26c90ed
│  │  ├─ 09
│  │  │  └─ 09271ca32c7c0d8f065114f815b00dcbba2315
│  │  ├─ 0a
│  │  │  └─ 5568b3eb72786b7d025f317905c26d9b2a59ce
│  │  ├─ 0e
│  │  │  ├─ 048441597444a7e2850d6d7c4ce15550f79bda
│  │  │  └─ 9b765676119956577706349c210e7fcdd7c69a
│  │  ├─ 0f
│  │  │  └─ b0cc2a6d677785c37d0b48490f3a8c43c7d49a
│  │  ├─ 10
│  │  │  └─ d0bdad6dff37ad6849a4e7bd753ada1ea64400
│  │  ├─ 12
│  │  │  └─ 293ab192a90ead99b571f3db22c172e400fe67
│  │  ├─ 13
│  │  │  ├─ 101ec102f48cd543c3f589c2e5c66f5603a17a
│  │  │  └─ 87725c4d3ba91e724a5b66fe4df86142f941e3
│  │  ├─ 15
│  │  │  └─ b952845ce2ee1dc8beb5de04d6bb5e6295ca12
│  │  ├─ 16
│  │  │  ├─ 0fb145edf2e28e22634019152457f0a7332f65
│  │  │  ├─ 6a00092986023c48b5c9d6f9c6e297eadb72b3
│  │  │  ├─ 6e691d5a8a499ecfe56658739acda2262a4b75
│  │  │  ├─ ae782a1b769d199f4c24a1701cbef84904224e
│  │  │  ├─ b3242c031802a1a5bc1f1ec780cadc920fbe13
│  │  │  └─ f5e97974dd7a08450a41598ab98b3d94f801c9
│  │  ├─ 17
│  │  │  ├─ 8c65bdeca9891c2b2bb31b058ecf325f8cb665
│  │  │  └─ 97c1e33af52697493bf3ffb3d5b748acf87ca8
│  │  ├─ 18
│  │  │  ├─ f51607af897f2fadf85d8234fb3826b8a14969
│  │  │  └─ f9e3d84f2c704d2c102febae5591dce1a7a4c0
│  │  ├─ 19
│  │  │  ├─ 9b93f941e5102a5ec6091c1779744cf5aba885
│  │  │  └─ ffe71bcbbeed2fd29deedd92c1a4c98fb7be3b
│  │  ├─ 1a
│  │  │  ├─ 3480df24d3a3014a92eace27c3ef295a05fe26
│  │  │  └─ 63eba617e9280b58daa720dffe79212503e4e3
│  │  ├─ 1b
│  │  │  ├─ 117ba9a4f0cca89145f6f1a38c6acc24e535df
│  │  │  ├─ 4e3bbbe7b291f4f24d23e17e2cc350a9ec4a2c
│  │  │  └─ c96d19fe4d0da8cdfeb04f365e8e92b0eb495a
│  │  ├─ 1c
│  │  │  ├─ 0ca3a549dbc5f6a97376bdbddd6b1b4e1eeba1
│  │  │  ├─ 1e81a4dbedff3f014459f5d6ae8d550d80e719
│  │  │  ├─ 2b62e2af7051df1531df74026de99312f4ce0b
│  │  │  ├─ 3390c40214dffd22ddfc57c7c7af418edcf1a4
│  │  │  ├─ bd484b5166cd963f0dd3c22e6e38a459fca484
│  │  │  └─ e835e1c30db2751ac2d76968ba1fcf5fbc23c3
│  │  ├─ 1d
│  │  │  ├─ 2466fc4ce637d312a45279bbf5dbcb13660e23
│  │  │  └─ b0bac66db394b86080382fe3336fbd693d1e72
│  │  ├─ 1f
│  │  │  └─ be1608a51d177ada85c02e61521f56a3d09d6a
│  │  ├─ 20
│  │  │  ├─ 110541d2f1b56a204baca882da776ceeea9470
│  │  │  └─ 3afbb1970bd1ced4e91186de793bd7fd794f96
│  │  ├─ 21
│  │  │  └─ a9b30ea11a8ffcdbeb13b7e7f7a54d2d16ad98
│  │  ├─ 22
│  │  │  └─ 3199a2400aa383fd95397f9a6c8c546e6dfca9
│  │  ├─ 23
│  │  │  ├─ 2566017ab20765eae2f01c989908f516559e4f
│  │  │  └─ 2a88158c6f77397da29b2aac5e1d4191e50194
│  │  ├─ 24
│  │  │  ├─ 2178d66fd937e95ad5c6dce3711053f7900391
│  │  │  ├─ 45c9dac492b375c80ba2c29ca686842d3dc7a0
│  │  │  └─ 79f878fde6af53cd248a0ea5f05df3239b01f2
│  │  ├─ 25
│  │  │  ├─ 69b9eab47a44d25d5bf84ccba0f32eb70e1e45
│  │  │  └─ 7e119e2c2c26918a3658f99308d805ddc8ebf0
│  │  ├─ 26
│  │  │  ├─ 8b767a6f09ab82fc47264aa3fbfa50d9bb9aaf
│  │  │  ├─ ca01ace22dd213c44d5b6336a7fa89ced37602
│  │  │  ├─ de4f89d4f3ce51c55f2d2ed5beaf510bdc802b
│  │  │  └─ f88bfaf05e98067c3634f5b60329cb2a3c568c
│  │  ├─ 27
│  │  │  └─ 86c8fe8c7f742c111190587283d1909f3ac4a5
│  │  ├─ 28
│  │  │  ├─ e4db5a67d2d917e05d557e254e4edb256d2f0f
│  │  │  └─ fdb0bbe28b1420f57567e25cf1b5b10b60a93e
│  │  ├─ 29
│  │  │  ├─ 6a895a35023743b5663dd835e9acaff763187d
│  │  │  ├─ a1566e7ec10fc82cd9102258c890bd9019e79d
│  │  │  ├─ a8859b2a7b8c97bd295d24d2d5373af8beef1e
│  │  │  └─ ce8514a4a4693c1170ee272c18b6cd716192b6
│  │  ├─ 2a
│  │  │  ├─ 2e193f70ff4f57cf6f55ac3af54a5566b90346
│  │  │  ├─ d206cbb21d13fff7df169cbe169786c92952bc
│  │  │  ├─ dc1f8980cbfbc826daa4df7a5971597040168f
│  │  │  ├─ eb6f22453bd8e68a3dbdb10c071c764cbf51fe
│  │  │  └─ f69862f87db69e0a99c1ff4bf3d4e7f8ec0092
│  │  ├─ 2b
│  │  │  ├─ 036cabbfa2dd160b6d4275495d91a09e73b31f
│  │  │  └─ 44233cf6f1a90a56638c9d72ad2c821083bd47
│  │  ├─ 2c
│  │  │  ├─ 0156303a8df3ffdc9de87765bf801bf6bea4a5
│  │  │  ├─ 24d9ccd779450204669c5a8e98234ffa3a0778
│  │  │  └─ 969eb04ad62529554bad1977b22c125c8db809
│  │  ├─ 2d
│  │  │  ├─ 5432e6c66494cf39f67f1aa1f697f40a9f8652
│  │  │  ├─ f64aa226de4c188a5666f105141ba89215cb2c
│  │  │  └─ ffcd10c2afca8a1ebddb4604c3f509a67f5f07
│  │  ├─ 2e
│  │  │  ├─ 2f70e3fcc80f51642871d86abffd0637c30356
│  │  │  └─ ea525d885d5148108f6f3a9a8613863f783d36
│  │  ├─ 2f
│  │  │  └─ 82e481c635d9a5e87e8e8b2a115ea64a3202cf
│  │  ├─ 31
│  │  │  ├─ 9888ad5741daad9825fced4936939f7f02aab1
│  │  │  ├─ 9b50292dc95b492489e2b285ca9e0d7eec9e52
│  │  │  └─ b4d0291afc5a4b6924ae2152aa7a58df18f1bf
│  │  ├─ 32
│  │  │  ├─ 0ee0ce221bc31fc632ac1f8d819e9234ab2935
│  │  │  ├─ 411a96c5923e7069ddb10ed2b14ad51c81c338
│  │  │  ├─ ba5cbd57e6db6127d19bc8aa51a53fff6e3155
│  │  │  └─ d6cbd7d3930fc897678fd797e4ac26e776ac77
│  │  ├─ 33
│  │  │  ├─ b421df0b835fc9054fe99d06c56d29731b94d3
│  │  │  └─ d12bd0fdd9f55c6853290d2b49e99786fca860
│  │  ├─ 35
│  │  │  ├─ 7d5c91a115f429ca300a39db3e320e0c2c399a
│  │  │  ├─ 8b7b433da715cd6c17c25f893c28f1cf28e584
│  │  │  └─ a7fb82740a5e6db258b67e76c1144b04752e68
│  │  ├─ 36
│  │  │  ├─ 20aec2c203d1295346d536565d169848819cc0
│  │  │  └─ 93819dcd9bc8ca0062b551becfeec476f87e80
│  │  ├─ 37
│  │  │  ├─ 271e2740d27b24f022ba51132bcb57ae25ef03
│  │  │  ├─ 90254d0907dbb1c7f30661e9d081722289c403
│  │  │  ├─ 930fed68c11328d5bb5b00fb6eba7659962dac
│  │  │  ├─ 93f531cc85b0c7426419afd3f636544264cc9c
│  │  │  └─ becb29057ae6425d7a503e2c03e2355967169f
│  │  ├─ 38
│  │  │  └─ eef7890ebb32f134e069ca1c8ba9dd8b88f754
│  │  ├─ 3a
│  │  │  └─ ce09a946a0756aec5af49a4a9237064d0f68ae
│  │  ├─ 3b
│  │  │  ├─ 3197f7f788aa7113faa142dff9db61d9323cd4
│  │  │  └─ eaf2e3a8b68d13da5138895935346f752387df
│  │  ├─ 3c
│  │  │  └─ d140f552d7c80ff68b1aee1fcbbb5e4226ce08
│  │  ├─ 3d
│  │  │  ├─ 3f49895293cc5a48c1270423a3da759c26914e
│  │  │  └─ 921a49f1a0d1507417db7eef411a315cbab379
│  │  ├─ 3e
│  │  │  ├─ 6c65c141378a702a5f3d72ad1f6193b5aee26a
│  │  │  ├─ 6c9002f107490582dad85eb9e01eea4e3de45b
│  │  │  └─ de57587189d660202a65e468fa204596ac0201
│  │  ├─ 3f
│  │  │  ├─ 97e64c0a12b7626c1e0ea39118d1394b97e60c
│  │  │  ├─ f1d67a155495f17c49e4d1adc12fac60a0729d
│  │  │  └─ f5b7b3439a3366fd3909786f4ff7eda79e31f3
│  │  ├─ 40
│  │  │  ├─ 17a9189aada389a5fad796a4c24e5cdaca301c
│  │  │  ├─ ac0ebcce731501d529f0643c01437b3e7943bf
│  │  │  └─ b27687d72a378bbf5749cf2d53a4949cdb6503
│  │  ├─ 41
│  │  │  ├─ 9fc1f7b3b6179844455ffd96d5610d8a05130f
│  │  │  └─ e6b6d9b37c6279d3d580469e232d31ef970d60
│  │  ├─ 42
│  │  │  ├─ 0186eb8179b6c326e6c74d3c4ab77849b1176f
│  │  │  └─ 71c3fdc2e1b9a3e32e8e1cc9bd9a5578468e5f
│  │  ├─ 44
│  │  │  └─ 948ca0857b083429f67551d482a9e2858a0163
│  │  ├─ 46
│  │  │  ├─ a15939a1d46888677b86e306e09e8cf44b8608
│  │  │  └─ c836abf9f5b9789375f56dd075b8e3ad5ea9ba
│  │  ├─ 48
│  │  │  └─ 7fa03bb72819b7569a76d84d20f991e9244136
│  │  ├─ 4a
│  │  │  ├─ 7c13b1b1e117eb023c09c5e9b4b57e2be5f674
│  │  │  └─ e5ce0cc500cf15405c20f5b53a59171f119b62
│  │  ├─ 4c
│  │  │  ├─ 313c108854866e5b94d0049be44532b32a2aa8
│  │  │  └─ 9709271b2ff28271b13c29bba5c50b80fea0ac
│  │  ├─ 4d
│  │  │  └─ 76ea6af5987622b7cefb2a5a779514e4667d23
│  │  ├─ 4e
│  │  │  ├─ 48fff6d5dd34b38ef01651e163c058b3febca4
│  │  │  └─ 99d8a3977ba839e25b48b172839adb47a39f77
│  │  ├─ 4f
│  │  │  ├─ d4de4d677120a830b1446ab08126c24e01df87
│  │  │  └─ e155833925c42b676bb98dc703d09fc689f00e
│  │  ├─ 50
│  │  │  ├─ 3de86c05042ef8fe6aa40b035e0445bb9a1511
│  │  │  └─ bc49610fc2f3969b1a5b4950979d92c972de1a
│  │  ├─ 51
│  │  │  ├─ 16ed3aa68af8c24467840b046e206d01d860c5
│  │  │  ├─ 1a606818b21ba58bb7be5d3e557e0bf471f1dc
│  │  │  └─ 228d133d55021c38f68bd8314195e6a22799d9
│  │  ├─ 52
│  │  │  └─ 99014c713fa930bcb1cd85f76397320528a4c6
│  │  ├─ 53
│  │  │  ├─ b1246408eb6b90a193c79fe9cc68c2019f7626
│  │  │  └─ cba59aaf0307f0833c8a62e51fd4d7458147dc
│  │  ├─ 54
│  │  │  ├─ 752e167d1fd323ee3465b66e237866d2981616
│  │  │  └─ f57b18cb30df8249a16c95f19480263f475c62
│  │  ├─ 55
│  │  │  ├─ 47086855e77a3100bf140467c78a6e60f20879
│  │  │  ├─ 7b5326db1740d759ddeb9593cf454b3666e46d
│  │  │  └─ b194295b0fa5a684bd86163608e68306a3be63
│  │  ├─ 56
│  │  │  └─ c4b9f03a683ffba80581ce2736c45ed5905240
│  │  ├─ 57
│  │  │  └─ 5f827c38cbb38af373af34ebdcd5053ecfdaca
│  │  ├─ 58
│  │  │  └─ b4d04fe2adeafa06159819171aa30c27815909
│  │  ├─ 59
│  │  │  └─ 8fd03a1729814cbd1dc86e156677e4c845b61b
│  │  ├─ 5a
│  │  │  ├─ 36f461eb003a45a6c2be4756ffee3da860e592
│  │  │  ├─ e403202eba7773b47749545d51d5fb1badc415
│  │  │  └─ e713df0977f0962b9c28209e0f20abd392ed06
│  │  ├─ 5b
│  │  │  ├─ 24d42e0b38910e32c581b41b337383895ccf7d
│  │  │  └─ 4b9a531329eb679dcd823e5550b22746853f8b
│  │  ├─ 5c
│  │  │  ├─ 41d2ee4d8e24617426d0edd45c911218d90908
│  │  │  └─ ae4c0a16bee74e8792f0688a7c9aefa04438e4
│  │  ├─ 5d
│  │  │  ├─ 108e2c7274693a25dce15c40aaba5772aa9382
│  │  │  ├─ 695ba0ab927f810e9480fa73b634fa979732f9
│  │  │  └─ 6fea80642dfb20098b33407d6c812cc8a925cc
│  │  ├─ 5e
│  │  │  └─ e3917e5a22214fcfaffe390ba9a19ec767ce4c
│  │  ├─ 5f
│  │  │  ├─ 2317161d8e447a7dd8017bb8a67cd7579a4d7a
│  │  │  ├─ 4a57522a05e083e6775a8d896cef43de57ea6f
│  │  │  ├─ 7067fea959d34324f48876fdd893e302d76cc3
│  │  │  ├─ 892d8992dd1fa5d734c032f733753e31ad37cc
│  │  │  └─ a510cffb7e83d64c7dd3062cd766afc97a735d
│  │  ├─ 60
│  │  │  ├─ 1d557efd506bae58d9e61ca0863ad0cbf472a3
│  │  │  └─ e6031438a985ea6cb9694e6a734e0a467dae0a
│  │  ├─ 61
│  │  │  ├─ 467009c14767c751a64e645b1d715dec8287a0
│  │  │  └─ 93df5e6e489ee4ab0248d8c832135346df0370
│  │  ├─ 62
│  │  │  └─ 16a6ac1b3676da22447bb7ee91c01023b82191
│  │  ├─ 63
│  │  │  └─ 1d0fba35ec5466e069f17f64d64028b1b4d487
│  │  ├─ 64
│  │  │  ├─ 2456c07c5928403f38a654f12cf12764c2b778
│  │  │  └─ c6fa9cb1a1d48a26ac130b829338e0a2580009
│  │  ├─ 65
│  │  │  ├─ 33e6e6bf890a8418040ea93cca761988261e3c
│  │  │  └─ f66559cb0a41a12885f1d3d716a9aee4a7063c
│  │  ├─ 66
│  │  │  ├─ a359df42100dd207905edbe19b682f6d99fec6
│  │  │  └─ ee54632f77afd18e54d8ec9c7ef9cecde895a8
│  │  ├─ 67
│  │  │  └─ 1b908d5941d734e3f412fc073c398fe2026ede
│  │  ├─ 69
│  │  │  ├─ 0caadb587912b646c87f9378215f39c75c7d21
│  │  │  ├─ 2d17dde65d9acf3bf0f28461732e7083bbf4eb
│  │  │  ├─ 453c648e1186bdffa28eae72beebed05e19388
│  │  │  └─ da9e318c1e1dbce0b351f477cc82b4fad027ef
│  │  ├─ 6a
│  │  │  ├─ 1aa0792d21d56487730d75ec1290fa0240b8cc
│  │  │  ├─ bbdd8f5a2bd2c99de6e110a7a4a9239fa18127
│  │  │  └─ d909c1151e952e7c866dc2bca64af0ca52b2e6
│  │  ├─ 6b
│  │  │  ├─ 1602f318e8f4168930d60e15a4cd6a1a422585
│  │  │  ├─ 6edaf6514d887da6c044acf77912fac3c2091c
│  │  │  └─ ac947a9acce7536e356233d4575547bb9b134f
│  │  ├─ 6c
│  │  │  ├─ 65f5324885c3e78fb3325ddde66a5d21aa203e
│  │  │  └─ bcfb2fe2735a7770d8193f514fcba227cac6b9
│  │  ├─ 6d
│  │  │  └─ 44b8abd3259b5205584f1b1ae13aab233d7295
│  │  ├─ 6e
│  │  │  └─ 99eb4bdd29a8d1d98c22b6c5c997862e3a99c9
│  │  ├─ 6f
│  │  │  └─ d48faa4cbaf4ea2a6d2405912980d5aa5f07e4
│  │  ├─ 70
│  │  │  └─ 6335be2071102f491a2ea396486ee86c8d7f18
│  │  ├─ 71
│  │  │  ├─ 16189103203109cea2b5c33b59cec4c493b0ae
│  │  │  └─ a0bfd299fc114fc2506938c606e604dc195ff5
│  │  ├─ 73
│  │  │  ├─ 53011ca8f8fad05e5f36fe75c63cd579fa05b0
│  │  │  └─ cacf2912187c9715a07997372e34db56b0d407
│  │  ├─ 74
│  │  │  ├─ 5c42f17274c33a8802c52648cc05a2cacd04f7
│  │  │  ├─ c613c5aa55fa55930cf43f16a5b424dd353ed5
│  │  │  └─ f8679c4bf99e8e384a3adf9a3c0a383348709c
│  │  ├─ 75
│  │  │  └─ 48488e4d0c1ef53a8797ae85c0bed55727defc
│  │  ├─ 76
│  │  │  ├─ 968fc2d06b0eb6ec47e8a3ae3c5bdefdcf8717
│  │  │  ├─ b110018cac74f43521b16b3cb418669210fbb8
│  │  │  └─ fdd39d19120ab596af0484bfe9c595d57213d2
│  │  ├─ 77
│  │  │  ├─ 20124e0c8c67b48ad0f19c4249382e436c776f
│  │  │  ├─ 4ebece60c6b9e15e03b2aedca09e696b0637fa
│  │  │  └─ 7be462f04017c269f92f161d5265056efb68f0
│  │  ├─ 78
│  │  │  └─ e6da69e102bbe69c350a88144942523e31c78c
│  │  ├─ 79
│  │  │  └─ ad8359cd5bdce316fbf96b83b3dd38d38300c9
│  │  ├─ 7a
│  │  │  └─ c32ebf5e18a114a1f92ed25d9fe6cfaa73901e
│  │  ├─ 7b
│  │  │  └─ 29b56c4bf340bff78e64745447eec0efe041db
│  │  ├─ 7d
│  │  │  └─ 124a93893d1224e9c7c06c4a428574e210b9c5
│  │  ├─ 7e
│  │  │  └─ 8d158492d2db44670238eebfe81581336d2645
│  │  ├─ 7f
│  │  │  ├─ b9f1b17124e984c793d63add96971a638de522
│  │  │  └─ c8ccb56d0703c89a04c58b80a0aba7bd505412
│  │  ├─ 81
│  │  │  ├─ 18fed245704ae5edb7624c51e9731cf66481e4
│  │  │  ├─ 9dd80f2a29da9e4f580b93dfe4098c228fcadf
│  │  │  └─ f5682488f2257348352e6c85162b3d2389e9ff
│  │  ├─ 82
│  │  │  ├─ 23e53f09e045e6e997b3e3aa6fc5f11fe910e6
│  │  │  ├─ b7f34c78e1cceb2bc5ba0f932d908f645df8f4
│  │  │  └─ e8413220636625174618ab0e2aab9f034388db
│  │  ├─ 83
│  │  │  └─ ea13e26d58e2b494f50a8f0e79b2c6e3e3b218
│  │  ├─ 84
│  │  │  ├─ 155f6b95252684015058f9fd0a8d674f00073d
│  │  │  └─ 3ef3617cde743500d431f7bc25261555b20bf2
│  │  ├─ 87
│  │  │  ├─ 48dc87709301eff10d801e14b0bf84eccb2096
│  │  │  ├─ 587852612a07e3e853558f0d7d0bf8993f3aa5
│  │  │  └─ 68a934685df57fcaf639ffb9755b47772b38f0
│  │  ├─ 88
│  │  │  ├─ 8ebc10c226da9fc6ad95ccd8c07abe6f9b7cc9
│  │  │  └─ 97ab297c333970b5b8101880ec697984ba6178
│  │  ├─ 89
│  │  │  └─ bba243e26e70d5d360fd33529cc0fda04b34f8
│  │  ├─ 8a
│  │  │  └─ 0d4ec2fd4649e1ac062fdb019c186a04f96c80
│  │  ├─ 8b
│  │  │  └─ ba287c4d6db70f72f16ee52d9caed55d8347ee
│  │  ├─ 8c
│  │  │  ├─ 834210f01c2b9af4d0a62561a92117a1a751cb
│  │  │  ├─ b941091329dbe93a60d6aa458c93e6154ecbd0
│  │  │  └─ e716a6caecc0cf8fd8a38aa998c6f4d06d186c
│  │  ├─ 8e
│  │  │  ├─ 0b23c67398c8bbcae4143bfef4448051e6f2f7
│  │  │  ├─ 355092cf277251d30341ded88e5807d0480a72
│  │  │  ├─ 74baf7405060dbe95228689dce8eafea519a33
│  │  │  └─ 7f3593a74119a64f53d40befb3982f2399c047
│  │  ├─ 8f
│  │  │  └─ 10ec6244c0840b9d031b29340ae508de290129
│  │  ├─ 90
│  │  │  └─ f333af605700726c82b09b29d80c66efb102e8
│  │  ├─ 91
│  │  │  ├─ 4585084e12bc34e35a17600fac5598a7f27090
│  │  │  ├─ a0990919ad3da35c4d69ad8b71c6f6d8e074dd
│  │  │  └─ b472ba597de337c431ee8cde3ca6ff7f941527
│  │  ├─ 92
│  │  │  ├─ 574f5ca2397692984b47d19b744076d2f2ba10
│  │  │  └─ 92de03a87261a9b383d1aa3079c8aa5d3e7c30
│  │  ├─ 93
│  │  │  └─ e3b79a902a31f5b1c86a94f8656de2dded3670
│  │  ├─ 94
│  │  │  ├─ 33d5f4d21b23ba25982fa3497fad74368946fd
│  │  │  ├─ 66a70ca48939fa9d735d9badbd4c6d077108f5
│  │  │  └─ e5071c734620c6cbb1e3e70b78a2accc8599e3
│  │  ├─ 96
│  │  │  └─ 6f76af9434bc095157d676d27c0b8483e9ae43
│  │  ├─ 97
│  │  │  ├─ 04b6362ba21fee1f84bcedf3ba32c0ae58139b
│  │  │  ├─ 329cf516705a8a1f530813096b7bd5f5dfb94c
│  │  │  ├─ 4e4f4a9f890bdff09fe7307aea2658b0058be4
│  │  │  └─ fc98e02238462a815399973d94e87ec4d8817c
│  │  ├─ 98
│  │  │  └─ 44bc27d0afb23eaad6998ceb210502498c98cb
│  │  ├─ 99
│  │  │  └─ 22323eb2964e14a48702da113ebc9ba15ccb9f
│  │  ├─ 9b
│  │  │  └─ 9142b2052462557acc27e076337c90febfe2a2
│  │  ├─ 9c
│  │  │  └─ e92f4007cb57f7c7fdb81aba58ba187cf6f2b9
│  │  ├─ 9d
│  │  │  ├─ 2d4f844c6973e472a64cc617d800188bb87f1d
│  │  │  ├─ 58287ce1363ce6904c0dea88a2a8022e27036e
│  │  │  └─ 855d479752bf866587685ac5bcd6dc557971d4
│  │  ├─ 9e
│  │  │  ├─ 940b5b9a32a164c8a6d09d0c8b2b400d7ed43a
│  │  │  └─ f542786ce3a34223011bafdc3d2d26b23418e6
│  │  ├─ 9f
│  │  │  ├─ 758222b81e6d2aa0d2827504224e9b59d238e0
│  │  │  ├─ 804a255c3a8de680a77922f8f5f5f8fba4b4e0
│  │  │  └─ f83f0063fbd7fb6841b78ff91adcd948e5a54b
│  │  ├─ a1
│  │  │  ├─ 14ae16e65dd5ae85a2cac34f0f156f37c3b682
│  │  │  └─ 453cda5ed2b09aee9b86b72ea78aa6d28473ad
│  │  ├─ a2
│  │  │  └─ c6c08e9ca0f310f10d4935f4207b34161d6a74
│  │  ├─ a4
│  │  │  ├─ 3a5157d2ff873535ca601d34122c48434de9a6
│  │  │  ├─ 5d24b46287df0a173952372b81ef991226e17f
│  │  │  ├─ dcc8fae29e0b095bcfcb3eb5cebc19e2a1c591
│  │  │  └─ f3985f8f5228b33a37b58288bfc95ebf7d0f95
│  │  ├─ a5
│  │  │  ├─ a9397af538c5b9edaef543e3c650e6b7428229
│  │  │  └─ ac2b6e7f21b9d81c08bc5cf110db2489447646
│  │  ├─ a6
│  │  │  ├─ cdf8911d1c76828b8442c6e695052cd46dacd4
│  │  │  └─ fc9dba8b911399ccfb8ebc24e6e902c73e99e2
│  │  ├─ a8
│  │  │  ├─ 25896228ce22b4d8c4064f4bf7727bcd4785c3
│  │  │  └─ fba26bf5843e5c71dbb7348aaeae8c0477e1ec
│  │  ├─ ac
│  │  │  └─ 8dccdf525a5b48584b34b7d166235eebd70127
│  │  ├─ ae
│  │  │  └─ b6fc33fe2601a27625c0ecdb51192450e4cd81
│  │  ├─ af
│  │  │  └─ 403fefb5ffbfd79c556f4a7a144dc7d58a3f47
│  │  ├─ b0
│  │  │  ├─ 4472fa32bc856e98ae9f4b2b6eb0361a2340d8
│  │  │  └─ f3ebbaae55de25abe5e6da97e5f9a0b62ed1ba
│  │  ├─ b2
│  │  │  ├─ b5a02abf6529f9e0243cf0927d23903c3fb8df
│  │  │  └─ beb1699733586d591f3fc212f8613e3781d511
│  │  ├─ b3
│  │  │  ├─ 4700986ba8585f4a6386d5e7a073ded9610c9e
│  │  │  └─ 55282bb70004d78ee399d32cf5271f8e3c924f
│  │  ├─ b4
│  │  │  └─ 756e7d14acc76f447b0efc0c7e89fd9f768fc7
│  │  ├─ b5
│  │  │  ├─ 292d4d91cb52b892ebb62f7d8c5ad033b7f16a
│  │  │  ├─ 970343ec73f3e338c7dc9e0737e572c9af3952
│  │  │  ├─ a90a265f3c3de3db8e9b84ae3dda6a419acb0e
│  │  │  └─ ca52707c2d8603f89ad391961c4b15e8d099f9
│  │  ├─ b6
│  │  │  └─ 1a80c8dcce0f12e48d9afefe81b3837224d3a1
│  │  ├─ b7
│  │  │  ├─ 2e33651e267b29d18d29b1b0990552a220ff87
│  │  │  └─ d6d9800ba0cbabd1a7fa0a038491f9d0319035
│  │  ├─ b8
│  │  │  ├─ 1790d29f94d9a7e649447d56c8ff27a6b0ecfe
│  │  │  ├─ 468f51b963fff56ac2ea68a0c9c3407dfb9d93
│  │  │  ├─ ced3dfe22933298c642dde564d3c349602a46c
│  │  │  └─ ec4e6f99fd80be38e98c195ae208e663f92858
│  │  ├─ b9
│  │  │  └─ 6482068de7bbc35716e7711dc73d048de9d8db
│  │  ├─ ba
│  │  │  ├─ 6ff49854e111736be0b0691b3dd8a8aa973439
│  │  │  └─ 871da2c3c000b9fdea72062d90fca16ee16d5f
│  │  ├─ bc
│  │  │  └─ 4133e924767461306bcd9bb32e0308376ca8fb
│  │  ├─ bd
│  │  │  ├─ 6612c15c831d814111782a87e46e658e2f9ee4
│  │  │  └─ 8b4d3ccac12d16b5e810bcfbdb65021677bd91
│  │  ├─ be
│  │  │  ├─ 2b8ac7bdfb9b163dc419390cd855589826a096
│  │  │  └─ 8d9f8278eff6c20049b33c2fce3f96ff0a8716
│  │  ├─ bf
│  │  │  ├─ 160199b19c61772cb3f78a174d333b76e15cd8
│  │  │  ├─ 54d216cdffee0639cd9596397b911f03d3723f
│  │  │  └─ d41363319b573c3751bbec7ad3db13fd2aac4c
│  │  ├─ c0
│  │  │  └─ 79a01be276b9d8dedb47487e48805c0baca74d
│  │  ├─ c1
│  │  │  └─ 3c2ed759bab8e972f720cfa177b8af2cd6dd72
│  │  ├─ c2
│  │  │  ├─ 2d1097cdeb800dffb8de9ac6f2292618395d4b
│  │  │  └─ ea85aab902ce3adff7d595dd647afade5a7c17
│  │  ├─ c3
│  │  │  ├─ 0bc77106be72d1f03400e684ee384b4f381c16
│  │  │  ├─ 33fe5afd5bfb9dd418035323013d1584bec6d3
│  │  │  └─ 7cb9aea475cb1335d8c384f8816dd21c777e50
│  │  ├─ c4
│  │  │  ├─ 8e4cff454847e88e8f3bb98c801527368b68f1
│  │  │  └─ e7decee4bd8cb73e1b15a357b97afe3435361f
│  │  ├─ c5
│  │  │  ├─ 90567e8f327186a0c3c122af2f9d0419896ef6
│  │  │  └─ d4f9741157855e6d433617953ef24a97c1db42
│  │  ├─ c6
│  │  │  └─ 7fe95ffebb399d65e53c740ad34f5611d5a3ae
│  │  ├─ c7
│  │  │  ├─ 667f0895bdb69fb8baa9f8da43eb2331c15bff
│  │  │  └─ ed9b676e15b6f31db324428f86a0018dfb4ada
│  │  ├─ c8
│  │  │  └─ ce1a3ee74a3707d37678780507c32c53e1a04d
│  │  ├─ ca
│  │  │  ├─ 6b8f41781ea05b22400f20af39cb0908458d95
│  │  │  ├─ 9dec030f314218cf41138c6c968ba73200df40
│  │  │  ├─ b0109ddda1a825137485961e5c3882568e4cb3
│  │  │  ├─ fb6935410465525968852f5653fb9a9eddd42d
│  │  │  └─ ff779fc0b836e53d893452514a363c51566e82
│  │  ├─ cb
│  │  │  ├─ 7eaf8bcda7095e80c6c6971f8bd4f3cbf2ac49
│  │  │  └─ fda46ce4c690a2ab66ab7610827beeb7572492
│  │  ├─ cc
│  │  │  └─ ab55142b0930225c3813c37593aca9e5ed3b9d
│  │  ├─ cd
│  │  │  ├─ 266a035f66166cc8bd48b098d198d779118f1d
│  │  │  ├─ 2cf34e5d4a59f197e66ddbf0b96d7d7977cc06
│  │  │  ├─ 6211a0a77cc7224eddd1b77b0f6b02467b9ecc
│  │  │  └─ 653804f4cea5b129b9e888198547a7978ede23
│  │  ├─ ce
│  │  │  ├─ 180c19ff0a26a854b0d6546cf3fef36576a63a
│  │  │  ├─ 5b41460da6616f331577af336b484bdea1d887
│  │  │  ├─ 73c0213f24987ea847b7a3bee7355e8c18e894
│  │  │  └─ d85015bd9abf853bb38d91dce78f7232b2b6fa
│  │  ├─ cf
│  │  │  └─ a8b6e7d09f8e3230a979950e764052d6325dcd
│  │  ├─ d0
│  │  │  ├─ 9251dcb4463ea2680753b8f04e334f5d183340
│  │  │  └─ b5c8b290575bbc3969c9ade3f652b28d74c197
│  │  ├─ d1
│  │  │  ├─ a50310d997b860d15a131b64b23ea1b606f4dd
│  │  │  ├─ ce6cbae5ed016adb1ed95d732d48f9bb3e8509
│  │  │  └─ fc1ad8c039583d1c11e881e1677c7249c28b43
│  │  ├─ d2
│  │  │  ├─ 0c6b69dffca2cb7d828ddf29c768861e817848
│  │  │  ├─ d01cceeb1ddaeb060ed70235e23c24dfb66a79
│  │  │  └─ fa9a5c38a7a6d6c893be41e9b4680e91968d7b
│  │  ├─ d3
│  │  │  └─ 2a20ba25c9f700734033dec49a121d1799d0da
│  │  ├─ d4
│  │  │  ├─ 95d09826a950a7b057e8f32476f26845e950af
│  │  │  └─ bd1a428c3da811540d0d5a858c5b0ab6919871
│  │  ├─ d5
│  │  │  ├─ 3c14b0827eb72b4c6f8601cb834d8e0850d6d3
│  │  │  ├─ 6e97ed777ed1bf417da105ab39449a7fd503a8
│  │  │  └─ f04597c22c1b11366cecdcf12010e157135a02
│  │  ├─ d6
│  │  │  ├─ 15f13a7d8814f7afe48fe5b4158f648b71e84b
│  │  │  └─ 606f1b28dd3fc3d97ab558922fdc62282cbc5f
│  │  ├─ d7
│  │  │  ├─ 35bae56a084b30ed42a822bfe6be8693194c8c
│  │  │  └─ e636c87739f91c3b9eefb95aa435c21700a900
│  │  ├─ d8
│  │  │  └─ 5be205f79e40e4f74e9cc8f659902c57913f44
│  │  ├─ d9
│  │  │  └─ f5c0fe1338ee70c3082be624dcc149d423919c
│  │  ├─ da
│  │  │  └─ bff770019226a8fb27a0ebfc88948d627353b4
│  │  ├─ db
│  │  │  └─ 36910d5b3ac7725d3fe4814cc6fd5cfcf4e339
│  │  ├─ dd
│  │  │  ├─ 2446e8ffbf7c2ecdc29927c0b626730a8028b8
│  │  │  └─ eea5c97c67c04d1d5db86b7ebd82875110a851
│  │  ├─ de
│  │  │  ├─ 2b05ca722f8c4bcdb01da8a4822133785c1a1b
│  │  │  └─ a18ea785cb1af475c0288c33ace8d5e5b98092
│  │  ├─ df
│  │  │  ├─ 86bd35584ef1cfbfdbe73abb276f2ab255c515
│  │  │  └─ f28864995443f4277054639d787c6831c452d0
│  │  ├─ e0
│  │  │  └─ 14fab93832859e92e075e0a0374a9e9e4dec6d
│  │  ├─ e1
│  │  │  ├─ 662c9979e45b84214ed7e679ef6f3086293dab
│  │  │  └─ 688b5b5ddd03a0bebdeb91832739d69e998441
│  │  ├─ e2
│  │  │  ├─ 370ac39e6453ce4939279ea462a2a5b52502a6
│  │  │  └─ bdae83ec1278378a7982250748fc3d737992ee
│  │  ├─ e3
│  │  │  └─ 0fede16e5b2a477a746b2c1b2591569abbcdc3
│  │  ├─ e4
│  │  │  └─ c7c00654fe6cc8a806bf8d6f6f97f6ce125ab2
│  │  ├─ e5
│  │  │  ├─ 3debb8427d0f1632956b13b5ecdc8522ea7bf8
│  │  │  └─ b18caa61fe322048416a36f548fabed51d45cd
│  │  ├─ e6
│  │  │  └─ 9de29bb2d1d6434b8b29ae775ad8c2e48c5391
│  │  ├─ e7
│  │  │  └─ 2328b417b9b0c594953231ab96ec21e7123605
│  │  ├─ e9
│  │  │  ├─ 5d03143cdfd79357dceeabd036d8cfccca751f
│  │  │  └─ aba5289e3dbe88935f267a22ee7f803e01a8be
│  │  ├─ ea
│  │  │  └─ 7e092971602359ace107af8976a5b27c18b8ab
│  │  ├─ ec
│  │  │  └─ 9d45c26a6bb54e833fd4e6ce2de29343894f4b
│  │  ├─ ed
│  │  │  ├─ 53c311c6d6f847273be2016a0d998cc40b68f1
│  │  │  └─ 9c1a2b34a5771cb0825aaf829abef949d9fda0
│  │  ├─ ee
│  │  │  ├─ 3962dd88a4b9f825a2c45071f8133dd2922b42
│  │  │  ├─ c23c12a299fa66666246317a9d64e9d4196523
│  │  │  └─ f89c2fdff9e16c737aff35246ac23262b628b1
│  │  ├─ ef
│  │  │  └─ 99fb510835106fcd2d1837a0ac3a38917616df
│  │  ├─ f0
│  │  │  ├─ 05aa9baab49964e13dd29b9986ea33285331e9
│  │  │  ├─ 263ee19cf00bad893064761bfca1cb4f3ab338
│  │  │  ├─ 7e145a9c99388c06292c29d50dad59eddcb4d1
│  │  │  └─ b13d6f2a9e2ae530f20551b37f3fe890ed8823
│  │  ├─ f1
│  │  │  ├─ 8ed38a7c7e0207f12550f389f6ef22d07ce56a
│  │  │  ├─ e50ae9c6c7b0a93ee06234119d11aff3f917cc
│  │  │  └─ fd1c35ad8d93fcb4a9ad0270503e8b2dc9679e
│  │  ├─ f3
│  │  │  └─ 70fd9ebbded7a03812ecba8a505b7331a74a92
│  │  ├─ f4
│  │  │  ├─ 4a27fb364cc7732065475252457528e4d69ea6
│  │  │  └─ cc9fd0f5d5ffe0796945ee5b02b1701ccd59f1
│  │  ├─ f5
│  │  │  ├─ 6ff001f35cfc4485e02434cf08303cb17bfa86
│  │  │  ├─ 83b0c7847ed39dd156b81e1fe5de0e0eee1909
│  │  │  ├─ c8f9d6ce04b0ba081f4cc9a9ff45e787dbcd0d
│  │  │  └─ eddcfe2b79b44bc8242d7d00216ae287e9d4d3
│  │  ├─ f6
│  │  │  ├─ 695021003703a7e2082cf229711e1a8843a580
│  │  │  ├─ c74c53b7e378ac98c7315de2fcd3b33e46dfde
│  │  │  └─ dfea9bd4536cbf73d874f0a4d99b08970cc7fd
│  │  ├─ f7
│  │  │  ├─ 9b95a6d068aed8d43fe25d62fe280f2d776ef4
│  │  │  └─ c940852c7545647072ba823809be71932cd97b
│  │  ├─ f8
│  │  │  └─ 16268d94992c07beb034f90ebc1dd19949180e
│  │  ├─ fb
│  │  │  ├─ 05d15bb0f21973a33de1347740f3e6cb4d25fd
│  │  │  └─ ad841bc8555970cfa5af586cec0fd7dcaedc0c
│  │  ├─ fc
│  │  │  ├─ 4f9e5b485412f8a7d5c63289b16462c043cd91
│  │  │  └─ 6862c81e3e07356d9553afc95c8781f744e3a7
│  │  ├─ fd
│  │  │  ├─ c8486576d3e1b79043f4b8b572117abc975318
│  │  │  └─ e8bf09b6f153434c778bd359238782a3c47a26
│  │  ├─ fe
│  │  │  └─ 419c6db280e0b92f89c38ea7e85fe4672aed22
│  │  ├─ ff
│  │  │  └─ 7bcb7c87210110c1090a54007d43e87f21cf8a
│  │  ├─ info
│  │  └─ pack
│  ├─ ORIG_HEAD
│  └─ refs
│     ├─ heads
│     │  └─ master
│     ├─ remotes
│     │  └─ origin
│     │     └─ master
│     └─ tags
├─ .gitignore
├─ add_data.py
├─ app.py
├─ application
│  ├─ database.py
│  ├─ models.py
│  ├─ routes.py
│  ├─ variables.py
│  ├─ __init__.py
│  └─ __pycache__
│     ├─ database.cpython-311.pyc
│     ├─ models.cpython-311.pyc
│     ├─ routes.cpython-311.pyc
│     └─ __init__.cpython-311.pyc
├─ assets
│  ├─ books
│  │  ├─ images
│  │  │  ├─ book_image_1d3f902e.png
│  │  │  ├─ book_image_42a38e5f.jpg
│  │  │  ├─ book_image_e5ddf3c2.png
│  │  │  └─ use_case_-_admin.png
│  │  └─ pdfs
│  │     ├─ book_pdf_e775ed0d.pdf
│  │     └─ Report.pdf
│  ├─ non-fiction_6b18244e.jpg
│  ├─ Novels_82ca5398.png
│  └─ periodicals_e766235e.jpg
├─ components
│  ├─ Footer.html
│  └─ navbar.html
├─ instance
│  └─ database.sqlite3
├─ package-lock.json
├─ package.json
├─ README.md
├─ requirements.txt
├─ static
│  ├─ add_book.css
│  ├─ add_section.css
│  ├─ book_requests.css
│  ├─ display_section_books.css
│  ├─ edit_book.css
│  ├─ edit_section.css
│  ├─ footer.css
│  ├─ librarian_dashboard.css
│  ├─ librarian_nav.css
│  ├─ librarian_section.css
│  ├─ library_statistics.css
│  ├─ login.css
│  ├─ register.css
│  └─ user
│     ├─ user_dashboard.css
│     ├─ view_books.css
│     └─ view_sections.css
├─ templates
│  ├─ librarian
│  │  ├─ book
│  │  │  ├─ add_book.html
│  │  │  └─ edit_book.html
│  │  ├─ book_requests.html
│  │  ├─ librarian_dashboard.html
│  │  ├─ library_statistics.html
│  │  ├─ section
│  │  │  ├─ add_section.html
│  │  │  ├─ display_section_books.html
│  │  │  └─ edit_section.html
│  │  └─ view_request.html
│  ├─ login.html
│  ├─ register.html
│  └─ user
│     ├─ download_ebook.html
│     ├─ give_feedback.html
│     ├─ request_return_book.html
│     ├─ user_dashboard.html
│     ├─ view_books.html
│     └─ view_sections.html
└─ __pycache__
   └─ app.cpython-311.pyc

```