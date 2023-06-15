const express = require('express');

const app = express();
const port = 3000;

// 정적 파일 제공 (React 애플리케이션을 빌드한 결과물을 제공하기 위해 사용)
app.use(express.static('build'));

// API 엔드포인트
app.get('/api/message', (req, res) => {
  const message = 'Hello from the server!';
  res.send({ message });
});

// 기타 경로에 대한 핸들링
app.get('*', (req, res) => {
  res.sendFile(__dirname + '/build/index.html');
});

// 서버 시작
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
