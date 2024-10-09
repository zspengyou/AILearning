from bs4 import BeautifulSoup


# # Sample HTML string
# html_content = '''
# <table class="wrapped confluenceTable tablesorter tablesorter-default" data-mce-resize="false" role="grid"><colgroup><col><col><col></colgroup><thead aria-label="Use column header buttons to sort"><tr role="row" class="tablesorter-headerRow"><th scope="col" class="confluenceTh tablesorter-header sortableHeader tablesorter-headerDesc" data-column="0" role="columnheader" aria-disabled="false" unselectable="on" style="user-select: none;" aria-sort="descending"><div class="tablesorter-header-inner"><button class="headerButton">Name</button></div></th><th scope="col" class="confluenceTh tablesorter-header sortableHeader tablesorter-headerUnSorted" data-column="1" role="columnheader" aria-disabled="false" unselectable="on" style="user-select: none;"><div class="tablesorter-header-inner"><button class="headerButton">Label</button></div></th><th scope="col" class="confluenceTh tablesorter-header sortableHeader tablesorter-headerUnSorted" data-column="2" role="columnheader" aria-disabled="false" unselectable="on" style="user-select: none;"><div class="tablesorter-header-inner"><button class="headerButton">Notes</button></div></th></tr></thead><tbody><tr role="row"><td class="confluenceTd"><span style="color: rgb(0,0,0);">treatment__v</span></td><td class="confluenceTd">Treatment</td><td class="confluenceTd">aka 'Study Drug'&nbsp;</td></tr><tr role="row"><td class="confluenceTd"><span style="color: rgb(0,0,0);">serious_adverse_event__v</span></td><td class="confluenceTd"><p><span style="color: rgb(0,0,0);">Serious Adverse Event</span></p></td><td class="confluenceTd"><p><span style="color: rgb(0,0,0);"><strong>At 23R3</strong></span></p><ul><li>This went into use (no use up to then), as the signal of 'this form creates a safety case'&nbsp; (the old ae_* form/item in safety definition recordd)</li><li>Only one record - per study (by validations) allowed at the release</li><li>Future release will allow multiple of these</li></ul></td></tr><tr role="row"><td class="confluenceTd"><span style="color: rgb(0,0,0);">patient_characteristics__v</span></td><td class="confluenceTd"><p>Patient Characteristics</p></td><td class="confluenceTd">Demography - Gender, DOB</td></tr><tr role="row"><td class="confluenceTd"><span style="color: rgb(0,0,0);">medical_history__v</span></td><td class="confluenceTd"><p>Medical History</p></td><td class="confluenceTd">Repeating form</td></tr><tr role="row"><td class="confluenceTd"><span style="color: rgb(0,0,0);">in_case_of_death__v</span></td><td class="confluenceTd">In Case of Death</td><td class="confluenceTd">Death form (non-repeating) for autopsy, cause of death</td></tr><tr role="row"><td class="confluenceTd"><span style="color: rgb(0,0,0);">external_labs__v</span></td><td class="confluenceTd">External Labs&nbsp;</td><td class="confluenceTd">Typically a site linked</td></tr><tr role="row"><td class="confluenceTd"><span style="color: rgb(0,0,0);">drug_history__v</span></td><td class="confluenceTd">Drug History</td><td class="confluenceTd">23R3</td></tr><tr role="row"><td class="confluenceTd"><span style="color: rgb(0,0,0);">concomitant_medication__v</span></td><td class="confluenceTd">Concomitant Medications</td><td class="confluenceTd">Repeating form</td></tr><tr role="row"><td class="confluenceTd">comments_by_system__v</td><td class="confluenceTd">Reporter / Sender Comment by System</td><td class="confluenceTd"><span style="color: rgb(0,51,102);" title="">24R3</span></td></tr><tr role="row"><td class="confluenceTd"><span style="color: rgb(122,134,154);"><em>adverse_event__v</em></span></td><td class="confluenceTd"><p><span style="color: rgb(122,134,154);"><em>Adverse Event</em></span></p></td><td class="confluenceTd"><p><strong>Essentially deprecated at 23R3 </strong>- records using it were moved to serious_adverse_event__v .. i.e. duration rules about SAEs to themselves.</p></td></tr></tbody></table>
# '''



# Function to parse the HTML table and return values for a given column number
def get_column_values(file_path:str, column_number:int):
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all table rows in the tbody
    table_rows = soup.find_all('tbody')[0].find_all('tr')

    # Initialize a list to store column values
    column_values = []

    # Iterate over each row
    for row in table_rows:
        # Get all columns (td) in the current row
        columns = row.find_all('td')

        # Check if the column number is within the valid range
        if column_number < 1 or column_number > len(columns):
            return f"Column number {column_number} is out of range."

        # Append the value of the specified column (subtract 1 for zero-based index)
        column_values.append(columns[column_number - 1].text)

    # Join the column values with newlines
    return column_values

if __name__ == '__main__':
# Example usage
    column_number = 2  # Input column number (e.g., 2 for the second column "Age")
    values = get_column_values("sample_html.html", column_number)
    print(f"Values in column {column_number}:\n{values}")