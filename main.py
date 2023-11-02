import streamlit as st


dna_list = ['A', 'T', 'G', 'C']
mrna_list = ['U', 'A', 'C', 'G']

# mRNAに変換
def transcribe(dna):
    mrna = ''
    for d in dna:
        mrna += mrna_list[dna_list.index(d)]
    st.text(f'mRNA:{mrna}')
    return mrna


def codon(mrna):
    check = [] # コドン判定用リスト
    bp_count = 0
    bool_start = True
    bool_end = False
    for m in mrna:
        bp_count += 1
        check.append(m)
        if len(check)>3:
            check.pop(0) # リストの最初の文字を削除
        # 開始コドン判定
        if (check == ['A', 'U', 'G']) & bool_start:
            st.text(f'開始コドンは{bp_count-2}番目です')
            start_codon = bp_count
            bool_start = False
            bool_end = True
        if (check == (['U', 'A', 'A']or['U', 'A', 'G']or['U', 'G', 'A'])) & bool_end:
            st.text(f'終始コドンは{bp_count-2}番目です')
            end_codon = bp_count
            bool_end = False
    
    if bool_start:
        st.text('開始コドンが見つかりませんでした')
        return
    if bool_end:
        st.text('終始コドンが見つかりませんでした')
    else:
        codon_count = end_codon-start_codon # bpカウント
        if codon_count%3 != 0:
            st.text('DNAに欠損または挿入があります')
        else:
            codon_count //= 3
            st.text(f'コドン数は{codon_count+1}です')

# -------フロント-------
st.title('DNA ⇒ codon')
dna = st.text_input('DNAを入力してください',help='A,T,G,Cのみ入力可能です')
search_check = False

for d in dna:
    # ATGC以外が入力された時
    if d not in dna_list:
        st.error(f'{d}は使えない文字です', icon='🚨')
        search_check = False
        st.stop()
search_check=True

if search_check:
    with st.form(key='form'):
        mrna = transcribe(dna)
        codon(mrna)
        btn = st.form_submit_button('変換')





