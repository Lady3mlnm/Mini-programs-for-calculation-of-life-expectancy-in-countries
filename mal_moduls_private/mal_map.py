import pandas as pd

# list of European countries (simple) at https://www.mapchart.net/europe.html (68 in total)
ls_countries_Europe = ['Albania', 'Algeria', 'Andorra', 'Armenia', 'Austria', 'Azerbaijan', 'Belarus', 'Belgium', 'Bosnia_and_Herzegovina', 'Bulgaria', 'Croatia', 'Cyprus', 'Czechia', 'Denmark', 'England', 'Estonia', 'Finland', 'France', 'Georgia', 'Germany', 'Greece', 'Hungary', 'Iceland', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jordan', 'Kazakhstan', 'Kosovo', 'Latvia', 'Lebanon', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Malta', 'Moldova', 'Monaco', 'Montenegro', 'Morocco', 'Netherlands', 'North_Macedonia', 'Northern_Ireland', 'Norway', 'Palestinian_Territories', 'Poland', 'Portugal', 'Romania', 'Russia', 'San_Marino', 'Saudi_Arabia', 'Scotland', 'Serbia', 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Syria', 'Tunisia', 'Turkmenistan', 'Türkiye', 'Ukraine', 'United_Kingdom', 'Uzbekistan', 'Vatican_City', 'Wales']

# list of world countries (simple) at https://www.mapchart.net/world.html (but without states of USA and provinces of Canada) (203 in total)
ls_countries_world = ['Afghanistan', 'Albania', 'Algeria', 'American_Samoa', 'Andorra', 'Angola', 'Antigua_and_Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia_and_Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina_Faso', 'Burundi', 'Cabo_Verde', 'Cambodia', 'Cameroon', 'Canada', 'Central_African_Republic', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo', 'Costa_Rica', 'Cote_d_Ivoire', 'Croatia', 'Cuba', 'Cyprus', 'Czechia', 'DR_Congo', 'Denmark', 'Djibouti', 'Dominica', 'Dominican_Republic', 'Ecuador', 'Egypt', 'El_Salvador', 'England', 'Equatorial_Guinea', 'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia', 'Faeroe_Islands', 'Falkland_Islands', 'Fiji', 'Finland', 'France', 'French_Guiana', 'French_Southern_and_Antarctic_Lands', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guatemala', 'Guinea', 'Guinea_Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hong_Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Madagascar', 'Malawi', 'Malaysia', 'Mali', 'Malta', 'Martinique', 'Mauritania', 'Mauritius', 'Mexico', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nepal', 'Netherlands', 'New_Caledonia', 'New_Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'North_Korea', 'North_Macedonia', 'Northern_Ireland', 'Norway', 'Oman', 'Pakistan', 'Palestinian_Territories', 'Panama', 'Papua_New_Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Puerto_Rico', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Réunion', 'Saint_Lucia', 'Saint_Vincent_and_the_Grenadines', 'Samoa', 'Saudi_Arabia', 'Scotland', 'Senegal', 'Serbia', 'Sierra_Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon_Islands', 'Somalia', 'South_Africa', 'South_Georgia_and_the_South_Sandwich_Islands', 'South_Korea', 'South_Sudan', 'Spain', 'Sri_Lanka', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syria', 'São_Tomé_and_Principe', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Timor_Leste', 'Togo', 'Trinidad_and_Tobago', 'Tunisia', 'Turkmenistan', 'Türkiye', 'Uganda', 'Ukraine', 'United_Arab_Emirates', 'United_Kingdom', 'United_States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela', 'Vietnam', 'Wales', 'Western_Sahara', 'Yemen', 'Zambia', 'Zimbabwe']


# list of world countries with microstate at https://www.mapchart.net/detworld.html (244 in total)
ls_countries_world_microstate = ['Afghanistan', 'Albania', 'Algeria', 'American_Samoa', 'Andorra', 'Angola', 'Anguilla', 'Antigua_and_Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia', 'Bosnia_and_Herzegovina', 'Botswana', 'Brazil', 'British_Indian_Ocean_Territory', 'British_Virgin_Islands', 'Brunei', 'Bulgaria', 'Burkina_Faso', 'Burundi', 'Cabo_Verde', 'Cambodia', 'Cameroon', 'Canada', 'Cayman_Islands', 'Central_African_Republic', 'Chad', 'Chile', 'China', 'Christmas_Island', 'Cocos_Islands', 'Colombia', 'Comoros', 'Congo', 'Cook_Islands', 'Costa_Rica', 'Cote_d_Ivoire', 'Croatia', 'Cuba', 'Curaçao', 'Cyprus', 'Czechia', 'DR_Congo', 'Denmark', 'Djibouti', 'Dominica', 'Dominican_Republic', 'Ecuador', 'Egypt', 'El_Salvador', 'England', 'Equatorial_Guinea', 'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia', 'Falkland_Islands', 'Faroe_Islands', 'Federated_States_of_Micronesia', 'Fiji', 'Finland', 'France', 'French_Guiana', 'French_Polynesia', 'French_Southern___Antarctic_Lands', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea_Bissau', 'Guyana', 'Haiti', 'Heard_Island___McDonald_Islands', 'Honduras', 'Hong_Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Isle_of_Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macau', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall_Islands', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New_Caledonia', 'New_Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'North_Korea', 'North_Macedonia', 'Northern_Ireland', 'Northern_Mariana_Islands', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestinian_Territories', 'Panama', 'Papua_New_Guinea', 'Paraguay', 'Peru', 'Philippines', 'Pitcairn_Islands', 'Poland', 'Portugal', 'Puerto_Rico', 'Qatar', 'Reunion', 'Romania', 'Russia', 'Rwanda', 'Saint_Helena', 'Samoa', 'San_Marino', 'Sao_Tome_and_Principe', 'Saudi_Arabia', 'Scotland', 'Senegal', 'Serbia', 'Seychelles', 'Sierra_Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon_Islands', 'Somalia', 'South_Africa', 'South_Georgia_and_the_South_Sandwich_Islands', 'South_Korea', 'South_Sudan', 'Spain', 'Sri_Lanka', 'St_Kitts_and_Nevis', 'St_Lucia', 'St_Pierre_et_Miquelon', 'St_Vincent_and_the_Grenadines', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Timor_Leste', 'Togo', 'Tokelau', 'Tonga', 'Trinidad_and_Tobago', 'Tunisia', 'Turkmenistan', 'Turks_and_Caicos_Islands', 'Tuvalu', 'Türkiye', 'Uganda', 'Ukraine', 'United_Arab_Emirates', 'United_Kingdom', 'United_States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican', 'Venezuela', 'Vietnam', 'Virgin_Islands', 'Wales', 'Wallis_and_Futuna', 'Western_Sahara', 'Yemen', 'Zambia', 'Zimbabwe']


def bin_values_in_dataframe(df, selected_col, *, step=None, prec=2, fn_bin=None, tp_combine_bins=None):
    '''
    The function looks at vulues in one of columms in dataframe and assigns to these values bins/ranges (that will be used in legend on map)
    df: dataframe
    selected_col: name of column in dataframe
    step: one of values 0.5, 1, 2, None
        determs width of bins. In it is None than function fn_bin have to be given.
    prec: integer >=1
        presicion of the second value in legend record
    fn_bin: function
        Function that make binning. These function is required only if step in None or unexpected
    tp_combine_bins: tuple in the form (('5.0–5.49', '5.5–5.99'), '5.0–5.99') or None
        this tuple allows to combine several bins into one bin
    return: two-column dataframe
        The first column contains values in alanysed column. The second columns range to that these values belong
    '''
    
    # get only selected column
    filtered_df = df.loc[:, [selected_col]]   \
                    .sort_values(by=selected_col, ascending=False)

    # depending on step, use different functions for assingning values to bins
    
    if step == 0.25:
        addition = float("0.199999"[:prec+2])
        fn_bin = lambda x: f"{x * 10 // 2 / 5:.1f}–{round(x * 10 // 2 / 5 + addition, prec)}" if pd.notna(x) else pd.NA
    elif step == 0.25:
        addition = float("0.249999"[:prec+2])
        fn_bin = lambda x: f"{x * 8 // 2 / 4:.2f}–{round(x * 8 // 2 / 4 + addition, prec)}" if pd.notna(x) else pd.NA
    elif step == 0.5:
        addition = float("0.499999"[:prec+2])
        fn_bin = lambda x: f"{x * 4 // 2 / 2:.1f}–{round(x * 4 // 2 / 2 + addition, prec)}" if pd.notna(x) else pd.NA
    elif step == 1:
        addition = float("0.999999"[:prec+2])
        fn_bin = lambda x: f"{int(x):.1f}–{round(int(x) + addition, prec)}" if pd.notna(x) else pd.NA
    elif step == 2:
        addition = float("1.999999"[:prec+2])
        fn_bin = lambda x: f"{x//2*2:.1f}–{round(x//2*2 + addition, prec)}" if pd.notna(x) else pd.NA
    elif step == 2.5:
        addition = float("2.499999"[:prec+2])
        fn_bin = lambda x: f"{x*8//20*2.5:.1f}–{round(8//20*2.5 + addition, prec)}" if pd.notna(x) else pd.NA

    # assign values to bins according function
    filtered_df['group_label'] = filtered_df[selected_col].map(fn_bin)
    
    # if it is required to combine several bins to one, do this
    if tp_combine_bins:
        filtered_df['group_label'] = filtered_df['group_label'].replace(*tp_combine_bins)

    
    min_value = filtered_df[selected_col].min()
    max_value = filtered_df[selected_col].max()
    print(f"Range: {min_value:.2f} – {max_value:.2f}   " +
          f"({filtered_df[selected_col].idxmin()} – {filtered_df[selected_col].idxmax()})")
    print(f"Number of groups: {filtered_df['group_label'].nunique()}")
    print(f"Number of values: {len(filtered_df)}")

    return filtered_df
