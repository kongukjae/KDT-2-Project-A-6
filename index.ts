import express, { Request, Response } from 'express';
import bodyParser from 'body-parser';
import path from 'path';

const app = express();
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());


app.get('/', (req: Request, res: Response)=>{
  res.sendFile(path.join(__dirname, './index.html'))
})
app.get('/test.js', (req: Request, res: Response)=>{
  res.sendFile(path.join(__dirname, './test.js'))
})

// 서버 포트 설정
app.listen(8080,()=>{
  console.log('서버 실행')
});