<!DOCTYPE html>
<html>
<head>
  <title>${table}</title>
</head>
<body>
  <h1>${table}</h1>

  <table>
    <thead>
      <tr>
        % for header_item in table_info:
            <th>${header_item}</th>
        % endfor
        </tr>
    </thead>
    <tbody>
      % for item in response:
        <tr>
        % for i in range(len(table_info)):
            <td>${item[i]}</td>
        % endfor

        </tr>
      % endfor
    </tbody>
  </table>
</body>
</html>
